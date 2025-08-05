# Imports
import sys
from datetime import date, datetime

def main():
    birth_date = (validate_date(input("Date of birth: ")))
    print(birth_date)
    print(time_delta(birth_date))

def validate_date(birth_date):
    # datetime.datetime(year = year, month = month, day = day)
    year = birth_date.split("-")[0]
    month = birth_date.split("-")[1]
    day = birth_date.split("-")[2]
    # return f"{year}-{month}-{day}"
    return [year, month, day]

def time_delta(date):
    year, month, day = date[0], date[1], date[2]
    birth_date = datetime.date(year = year, month = month, day = day)
    return birth_date


if __name__ == "__main__":
    main()