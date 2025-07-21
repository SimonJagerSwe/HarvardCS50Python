# Imports
import re


# Main function
def main():
    print(time_conversion(input("Hours: ").upper()))


# Time conversion function, using regex
def time_conversion(s):
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) TO (\d{1,2}):?(\d{2})? (AM|PM)$", s)
    # Check if time variable is valid
    if time:
        # Divide up starting hours and minutes, and ending hours and minutes into variables
        starting_hour = int(time.group(1))
        print(starting_hour)
        # print(type(starting_hour))
        starting_minute = time.group(2)
        print(starting_minute)
        # print(type(starting_minute))
        starting_am_or_pm = time.group(3)
        print(starting_am_or_pm)
        # print(type(starting_am_or_pm))
        ending_hour = int(time.group(4))
        print(ending_hour)
        # print(type(ending_hour))
        ending_minute = time.group(5)
        print(ending_minute)
        # print(type(ending_minute))
        ending_am_or_pm = time.group(6)
        print(ending_am_or_pm)
        # print(type(ending_am_or_pm))

        # Check if starting hours are am or pm
        if starting_am_or_pm == "PM" and starting_hour <= 12:
            starting_hour += 12
            # print(starting_hour)
        elif starting_am_or_pm == "AM" and starting_hour == 12:
            starting_hour -= 12
            # print(starting_hour)

        

    else:
        raise ValueError("Wrong time format")





# Condition to run main function
if __name__ == "__main__":
    main()