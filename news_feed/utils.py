from datetime import datetime


def file_name():
    # get current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # the file name
    file_name = f"news_{current_date}.csv"

    return file_name
