# Imports
import sys
from datetime import date


def main():
    birth_date = (validate_date(input("Date of birth: ")))
    print(birth_date)


def validate_date(birth_date):
    year = birth_date.split("-")[0]
    month = birth_date.split("-")[1]
    day = birth_date.split("-")[2]
    if (
        len(year) != 4 or
        len(month) != 2 or
        len(day) != 2
    ):
        sys.exit("Invalid date format")

    else:
        # birth_date = f"{year}-{month}-{day}"
        # return birth_date
        return f"{year}-{month}-{day}"
    



if __name__ == "__main__":
    main()