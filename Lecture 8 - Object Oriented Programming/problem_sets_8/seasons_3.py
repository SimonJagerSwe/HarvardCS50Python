# Imports
import sys

from datetime import date, datetime

def main():
    current_date = date.today()
    print(date_check(input("Date of birth: "), current_date))


def date_check(b, c):
    # current_date = c
    # birth_date = b
    birth_date = date.fromisoformat(str(b))
    current_date = date.fromisoformat(str(c))    
    # print(type(current_date), type(birth_date))
    # print(date.fromisoformat(str(c)))
    print(current_date)
    print(type(current_date))
    print(birth_date)
    print(type(birth_date))
    delta = current_date - birth_date
    return delta

    # print(date.fromisoformat(b))
    # date_1 = datetime.strptime(str(current_date), date.fromisoformat)
    # return date_1
    
    


if __name__ == "__main__":
    main()
