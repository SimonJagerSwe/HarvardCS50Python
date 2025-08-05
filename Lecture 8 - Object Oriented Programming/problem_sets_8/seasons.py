# Imports
import datetime
import sys
# from datetime import date


def main():
    birth_date = (validate_date(input("Date of birth: ")))
    print(birth_date)
    print(convert_date(birth_date))


def validate_date(birth_date):
    year = birth_date.split("-")[0]
    month = birth_date.split("-")[1]
    day = birth_date.split("-")[2]
    if (
        len(year) != 4 or
        len(month) != 2 or
        int(month) < 1 or
        int(month) > 12 or
        len(day) != 2 or
        int(day) < 1 or
        int(day) > 31
    ):
        sys.exit("Invalid date format")

    else:
        # birth_date = f"{year}-{month}-{day}"
        # return birth_date
        return f"{year}-{month}-{day}"
    

def convert_date(birth_str):
    return datetime.date.today()

if __name__ == "__main__":
    main()