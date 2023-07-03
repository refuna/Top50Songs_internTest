from datastream import Country


def get_top_songs_sort(top_dict: dict, k=50) -> list[tuple[int, int]]:
    """ Return the top 50 songs for a given country. With a sorting algorithm (O(S*log(S))

    --- INPUT ---
    top_dict = dict {sng_id: count} }
    --- OUTPUT ---
    top_list = list[tuple[int, int]]

    """
    top = sorted(top_dict.items(), key=lambda x: x[1], reverse=True)

    # Print the top 50 songs for each country
    return top[:k]


def get_top_songs_linear(top_dict: dict, k=50) -> list[tuple[int, int]]:
    """ Return the top 50 songs for a given country. With a linear algorithm (O(S*k))

    --- INPUT ---
    top_dict = dict {sng_id: count} }
    --- OUTPUT ---
    top_list = list[tuple[int, int]]

    """

    top = []
    for _ in range(k):
        if len(top_dict) == 0:
            break
        top.append(max(top_dict.items(), key=lambda x: x[1]))
        top_dict.pop(top[-1][0])

    return top


if __name__ == "__main__":

    country_top = {Country.DE: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50},
                   Country.GB: {1: 30, 2: 10, 3: 20, 4: 50, 5: 40}}

    print("Test get_top_songs_sort")
    for country, top_dict in country_top.items():
        # Sort the top songs for each country
        # Complexity = O(S*log(S)) where S is the number of songs

        top_list = get_top_songs_sort(top_dict)
        print(f"Top 50 songs for {country.name}: {top_list}")

    print("Test get_top_songs_linear")
    for country, top_dict in country_top.items():
        # Sort the top songs for each country
        # Complexity = O(S*k) where S is the number of songs

        top_list = get_top_songs_linear(top_dict)
        print(f"Top 50 songs for {country.name}: {top_list}")
