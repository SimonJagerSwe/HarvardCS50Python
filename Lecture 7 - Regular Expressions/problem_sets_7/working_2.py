import re

def main():
    print(time_conversion(input("Hours: ")))


def time_conversion(s):
    # For first time, check if there are minutes present, if minutes are present, check that minutes are double digits, then find AM or PM, then repeat
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)


    # Check if time conforms to expressions
    if time:


        # Dividing time expression into up time variables
        starting_hour = int(time.group(1))        
        starting_minutes = int(time.group(2))
        starting_am_or_pm = time.group(3)
        ending_hour = int(time.group(4))
        ending_minutes = int(time.group(5))
        ending_am_or_pm = int(time.group(6))        


        # Check that minutes don't exceed 59
        if starting_minutes:
            if starting_minutes >= 60:
                raise ValueError
            if ending_minutes >= 60:
                raise ValueError
        

        # Check if starting hour is AM or PM, and checking against errors stemming from 12 AM
        if starting_am_or_pm == "PM":
            starting_hour += 12
        elif starting_am_or_pm == "AM" and starting_hour == 12:
            starting_hour = 00
        else:
            pass

        # Same for ending hours
        if ending_am_or_pm == "PM":
            ending_hour += 12
        elif ending_am_or_pm == "AM" and ending_hour == 12:
            ending_hour == 00
        else:
            pass


        # After validating hours, check for starting minutes
        if not starting_minutes:
            starting_time = (f"{starting_hour:02}:00")
        else:
            starting_time = (f"{starting_hour:02}:{starting_minutes}")
        
        # Same for ending minutes
        if not ending_minutes:
            ending_time = (f"{ending_hour:02}:00")
        else:
            ending_time = (f"{ending_hour:00}:{ending_minutes}")

        # Repeat above for finishing hours, not very DRY, but it's what I can get to work
         

            
    #  If time format doesn't align with expressions, raise value error
    else:        
        raise ValueError


if __name__ == "__main__":
    main()