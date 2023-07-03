from country import Country

def read_csv_with_error_handling(date) -> tuple[int, int, Country]:
    """
    Read a CSV file and yield each row as a tuple of (sng_id, user_id, country).
    If a row is invalid, print an error message and skip the row.

    --- Example ---
    Input:
        1|1|DE
        2|2|GB
        3|3|NL

    Output:
        (1, 1, <Country.DE: 1>)
        (2, 2, <Country.GB: 2>)
        (3, 3, <Country.NL: 3>)

    --- Input ---

    date: str
        The date of the file to read, in the format YYYY-MM-DD.

    --- Output ---

        tuple[int, int, Country]
        A tuple of (sng_id, user_id, country) for each row in the file.
    """

    file_path = f"..\data\sample_listen-{date}_2Mlines.log"

    with open(file_path, "r") as file:
        lines = file.readlines()
        for row in lines:
            try:
                record = row.strip().split('|')
                if len(record) == 3:
                    if record[2] not in Country.__members__:
                        raise Exception(f"Invalid country: {record[2]}")
                    else:
                        country = Country[record[2]]
                    sng_id = int(record[0])
                    user_id = int(record[1])
                    yield sng_id, user_id, country
                else:
                    raise Exception(f"Invalid record: {record}")
            except Exception as e:
                pass
                # print(f"Error: {e} - Skipping row.")


if __name__ == "__main__":
    date = '2021-12-02'
    for row in read_csv_with_error_handling(date):
        sng_id, user_id, country = row


