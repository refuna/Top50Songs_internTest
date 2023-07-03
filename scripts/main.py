from datastream import read_csv_with_error_handling, Country
from get_top import get_top_songs_sort, get_top_songs_linear
import joblib
import datetime

# Load past 7 days of country_top from disk
def load_past7days(date, mode = 'country'):
    """ Load the past 7 days of country_top from disk"""
    past_top = []
    for delta in range(7):
        current_date = datetime.datetime.strptime(date, '%Y-%m-%d') - datetime.timedelta(days=delta)
        previous_date = current_date.strftime('%Y-%m-%d')
        try:
            top = joblib.load(f'../records/{mode}_top_{previous_date}.joblib')
            past_top.append(top)
        except:
            continue
    return past_top

def merge_tops(all_ids, past_top):
    """ Merge the past 7 days of country_top"""
    merged_top = {}
    for id in all_ids:
        merged_top[id] = {}
        for top in past_top:
            if id in top:
                for sng_id, count in top[id].items():
                    merged_top[id][sng_id] = merged_top[id].get(sng_id, 0) + count
    return merged_top

def write_top(top, mode):
    """ Write the top 50 songs for each country to a file."""
    with open(f'../outputs/{mode}_top50_{today_date}.txt', 'w') as f:
        for id, top_dict in top.items():
            top_list = get_top_songs_linear(top_dict)
            formatted_string = ','.join([f'{sng_id}:{count}' for sng_id, count in top_list])
            if mode == 'country':
                f.write(f"{id.name}|{formatted_string}\n")
            else:
                f.write(f"{id}|{formatted_string}\n")

if __name__ == "__main__":

    today_date = '2021-12-02'

    # Create a dictionary to store the counts for each country
    country_top = {country: {} for country in Country}
    user_top = {}

    for row in read_csv_with_error_handling(today_date):
        sng_id, user_id, country = row

        # Populate country_top
        current_country = country_top[country]
        current_country[sng_id] = current_country.get(sng_id, 0) + 1

        # Populate user_top
        if user_id not in user_top:
            user_top[user_id] = {}

        if sng_id not in user_top[user_id]:
            user_top[user_id][sng_id] = 0

        user_top[user_id][sng_id] += 1

    # Save country_top and user_top to disk
    joblib.dump(country_top, f'../records/country_top_{today_date}.joblib')
    joblib.dump(user_top, f'../records/user_top_{today_date}.joblib')

    past_country_top = load_past7days(today_date, 'country')
    past_user_top = load_past7days(today_date, 'user')

    # Merge the past 7 days of country_top
    merged_country_top = merge_tops(Country, past_country_top)

    # Get all user ids
    merged_user_top = {}
    all_user_ids = set()
    for user_top in past_user_top:
        all_user_ids |= set(user_top.keys())

    merged_user_top = merge_tops(all_user_ids, past_user_top)

    # Save top_50_overlast7days to disk
    write_top(merged_country_top, 'country')
    write_top(merged_user_top, 'user')