# Imports
import re


# Main function
def main():
    print(time_conversion(input("Hours: ")))


# Time conversion function, using regex
def time_conversion(s):
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)

    # Check if time comforms to above regex
    if time:
        # Check if minutes are present in starting time
        if time.group(2):
            if int(time.group(2)) >= 60:
                raise ValueError("Can't have that many minutes, now can, we?")
            else:
                pass
        # Check if minutes are present in ending time
        if time.group(5):
            if int(time.group(5)) >= 60:
                raise ValueError("Can't have that many minutes, now can we?")
            else:
                pass
        

        # Create starting time, checking for possible errors concerning 12-hour format errors where time starts with 12
        starting_hour = int(time.group(1))
        if time.group(3) == "PM":
            starting_hour += 12
        elif time.group(3) == "AM" and starting_hour == 12:
            starting_hour -= 12


        # Starting time
        if time.group(2) == None:
            start_time = (f"{starting_hour:02}:00")
        else:
            start_time = (f"{starting_hour}:{time.group(2)}")

            
        # Create ending time, same as above
        ending_hour = int(time.group(4))
        if time.group(6) == "PM":
            ending_hour += 12
        elif time.group(6) == "AM" and ending_hour == 12:
            ending_hour -= 12


        # End time
        if time.group(5) == None:
            ending_time = (f"{ending_hour:02}:00")
        else:
            ending_time = (f"{ending_hour}:{time.group(5)}")

        time = (f"{starting_hour} to {ending_hour}")
        return time



    # If time does not conform to above regex, raise error
    else:
        raise ValueError("Wrongo!!!")


# Condition to run main function
if __name__ == "__main__":
    main()