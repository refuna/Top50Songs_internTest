
Objective
========================

The objective of this exercise is to suggest a system that computes on a daily basis, the top 50 songs the most listened in each country on the last 7 days, as
well as the top 50 songs (optional) the most listened by each user on the last 7 days.

Project Organization
-------------
    ├── data               <- Data from third party sources which contains sng_id, user_id and country ISO.
    ├── records            <- joblib files with the data sorted by country and user.
    ├── outputs            <- top 50 songs in each country over past 7 days and top 50 songs by each user over past 7 days on the specified format.
    ├── scripts
          ├── country.py         <- The Country class represents a set of countries, each with a unique identifier.
          │                       The countries included in the enumeration are Germany(DE), Great Britain (GB), Netherlands (NL), and Belgium (BE).
          ├── datastream.py      <- Read a CSV file and yield each valid row as a tuple of (sng_id, user_id, country).
          ├── get_top.py         <- Retrieve the top 50 songs for a given country using different algorithms.
          ├── main.py            <- Get the top 50 songs in each country and top 50 songs by individual users over past 7 days.

-------

#  Getting started

## Function
1. `load_past7days(date, mode = 'country')`
Loads the past 7 days of country_top (or user_top) data from disk. It takes the current date as input and an optional mode parameter, which determines whether it loads country based or user based data. It returns a list containing the top 50 songs data for each of the past 7 days.

2. `merge_tops(all_ids, past_top)`
Merges the top data from the past 7 days into a single dictionary. It takes all_ids (representing either the set of all countries or all user IDs) and past_top (the list of top data from the past 7 days) as input. It returns a merged dictionary containing the cumulative top data.

3. ` write_top(top, mode)`
Writes the top 50 songs for each country (or user) to a file. It takes top (the merged top data) and mode (indicating whether it is for country or user data) as input. It writes the top songs to a text file in the specified format.


## Usage
To run the script, simply open a terminal or command prompt window, navigate to the directory where the script is located, and type the following command:
`python main.py`

The main entry point of the code. It executes the following steps:

1. Sets the today_date variable to a specific date.
2. Initializes the country_top and user_top dictionaries.
3. Reads data using the read_csv_with_error_handling function, populating the country_top and user_top dictionaries.
4. Saves the country_top and user_top dictionaries to disk using the joblib.dump function.
5. Loads the past 7 days of country and user top data using the load_past7days function.
6. Merges the past 7 days of country data using the merge_tops function.
7. Collects all user IDs and merges the past 7 days of user top data.
8. Saves the merged sorted top data to disk using the write_top function.

------------------------------------
* Adjust the `today_date` variable in the `main` section to the desired date.
* Ensure that the necessary dependencies are installed and accessible.
Please note that the code assumes the existence of specific file and directory structures. Make sure that the directories (`../records/` and `../outputs/`) exist and have the required write permissions.

