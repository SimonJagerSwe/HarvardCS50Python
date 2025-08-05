# Imports
import inflect
import sys

from datetime import date


def main():
    current_date = date.today()
    birth_date = (validate_date(input("Date of birth: "), current_date))
    # print(birth_date)
    days = date_delta(birth_date, current_date)
    # print(days)
    minutes = (convert_days(days))
    # print(minutes)
    # song = convert_minutes_to_string(minutes)
    # print(song)
    print(convert_minutes_to_string(minutes).capitalize())
    # print(convert_minutes_to_string(minutes).capitalize())


def validate_date(b, c):
    if not "-" in b:
        sys.exit("Invalid date format")
    # current_date = datetime.date.today()
    # print(str(current_date))
    # print(type(current_date))
    year_string = str(c)
    current_year = year_string.split("-")[0]
    # current_month = str(date.today()).split("-")[1]
    # current_day = str(date.today()).split("-")[2]
    # print(current_year)
    # print(current_month)
    # print(current_day)
    given_year = b.split("-")[0]
    given_month = b.split("-")[1]
    given_day = b.split("-")[2]
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
        # return [given_year, given_month, given_day]
    

def date_delta(b, c):
    birth_date = date.fromisoformat(str(b))
    current_date = date.fromisoformat(str(c)) 
    # delta = current_date - birth_date
    # return delta
    # return f"{date_1} / {date_2}"
    return current_date - birth_date


def convert_days(d):
    hours = str(d)
    # print(type(hours))
    minutes = int(hours.split(" ")[0]) * 1440
    return minutes


def convert_minutes_to_string(m):
    p = inflect.engine()
    m = int(m)
    full_string = p.number_to_words(m).replace(" and", "")
    # return " ".join(word_list)
    return f"{full_string} minutes"

if __name__ == "__main__":
    main()