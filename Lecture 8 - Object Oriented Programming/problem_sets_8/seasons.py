# Imports
# import datetime
import sys
from datetime import date, datetime


def main():
    birth_date = (validate_date(input("Date of birth: ")))
    print(birth_date)
    print(convert_date(birth_date))


def validate_date(birth_date):
    # current_date = datetime.date.today()
    # print(str(current_date))
    # print(type(current_date))
    current_year = str(date.today()).split("-")[0]
    current_month = str(date.today()).split("-")[1]
    current_day = str(date.today()).split("-")[2]
    # print(current_year)
    # print(current_month)
    # print(current_day)
    given_year = birth_date.split("-")[0]
    given_month = birth_date.split("-")[1]
    given_day = birth_date.split("-")[2]
    if (
        len(given_year) != 4 or
        int(given_year) > int(current_year) or
        len(given_month) != 2 or
        int(given_month) < 1 or
        int(given_month) > 12 or
        len(given_day) != 2 or
        int(given_day) < 1 or
        int(given_day) > 31
    ):
        sys.exit("Invalid date format")

    else:
        # birth_date = f"{year}-{month}-{day}"
        # return birth_date
        return f"{given_year}-{given_month}-{given_day}"
    

def convert_date(birth_str):
    # datetime.date.today()
    # return
    pass

if __name__ == "__main__":
    main()