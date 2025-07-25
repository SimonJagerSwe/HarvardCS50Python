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
        # print(starting_hour)
        # print(type(starting_hour))
        starting_minutes = time.group(2)
        # print(starting_minutes)
        # print(type(starting_minutes))
        starting_am_or_pm = time.group(3)
        # print(starting_am_or_pm)
        # print(type(starting_am_or_pm))
        start_time = ""
        ending_hour = int(time.group(4))
        # print(ending_hour)
        # print(type(ending_hour))
        ending_minutes = time.group(5)
        # print(ending_minutes)
        # print(type(ending_minutes))
        ending_am_or_pm = time.group(6)
        # print(ending_am_or_pm)
        # print(type(ending_am_or_pm))
        ending_time = ""
        

        # Check if starting hours are am or pm
        if starting_am_or_pm == "PM" and starting_hour < 12:
            starting_hour += 12
            # print(starting_hour)
        elif starting_am_or_pm == "AM" and starting_hour == 12:
            starting_hour -= 12
            # print(starting_hour)

        # Check if there are starting time minutes
        if starting_minutes == None:
            start_time = f"{starting_hour:02}:00"
        else:
            if int(starting_minutes) > 59:
                raise ValueError("Wrong time format")
            start_time = f"{starting_hour:02}:{starting_minutes:02}"
            
        # return start_time

        # Check if ending hours ar am or pm
        if ending_am_or_pm == "PM" and ending_hour != 12:
            ending_hour += 12
            # print(ending_hour)
        elif ending_am_or_pm == "AM" and ending_hour == 12:
            ending_hour -= 12
            # print(ending_hour)


        # Check if there are ending minutes
        if ending_minutes == None:
            ending_time = f"{ending_hour:02}:00"
        else:
            if int(ending_minutes) > 59:
                raise ValueError("Wrong time format")
            ending_time = f"{ending_hour:02}:{ending_minutes:02}"

        time = f"{start_time} to {ending_time}"
        return time
    
        
    else:
        raise ValueError("Wrong time format")





# Condition to run main function
if __name__ == "__main__":
    main()