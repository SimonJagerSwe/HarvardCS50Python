# Imports
import sys
from datetime import date


def main():
    print(validate_date(input("Date of birth: ")))


def validate_date(date):
    year = date.split("-")[0]
    month = date.split("-")[1]
    day = date.split("-")[2]
    if (
        len(year) != 4 or
        len(month) != 2 or
        len(day) != 2
    ):
        sys.exit("Invalid date format")

    else:
        return f"{year}-{month}-{day}"


if __name__ == "__main__":
    main()