import re

def main():
    print(time_conversion(input("Hours: ")))


def time_conversion(s):
    # For first time, check if there are minutes present, if minutes are present, check that minutes are double digits, then find AM or PM, then repeat
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)
    # print(time.group(1))
    # print(time.group(2))
    # print(time.group(3))
    # print(time.group(4))
    # print(time.group(5))
    # print(time.group(6))


    # Check if time conforms to expressions
    if time:


        # Dividing time expression into up time variables
        starting_hour = int(time.group(1))
        starting_minutes = time.group(2)
        starting_am_or_pm = time.group(3)
        starting_time = ""
        ending_hour = int(time.group(4))       
        # ending_minutes = int(time.group(5))
        ending_am_or_pm = time.group(6)
        ending_time = ""

        print(starting_hour)
        print(type(starting_hour))
        print(starting_minutes)
        print(type(starting_minutes))
        print(starting_am_or_pm)
        print(type(starting_am_or_pm))
        print(ending_hour)
        # print(ending_minutes)
        # print(type(ending_minutes))
        print(ending_am_or_pm)
        print(type(ending_am_or_pm))

        # Check if starting minutes are present, and not exceeding 59
        if time.group(2) is not None:
            starting_minutes = int(time.group(2))
            if starting_minutes >= 60:
                raise ValueError
            else:
                starting_minutes = int(time.group(2))
    
        # Check if minutes are present in starting time
        else:
            starting_minutes = 00
            
        
        # Check that ending minutes don't exceed 59
        if time.group(5):    
            ending_minutes = int(time.group(5))
            if ending_minutes >= 60:
                raise ValueError
            else:
                ending_minutes = int(time.group(5))

            if not ending_minutes:
                ending_time = (f"{ending_hour:02}:00")
            else:
                ending_time = (f"{ending_hour:00}:{ending_minutes}")

            # Check if minutes are present in ending time
            

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


        time = (f"{starting_time} to {ending_time}")
        return time
         
            
    #  If time format doesn't align with expressions, raise value error
    else:        
        raise ValueError


if __name__ == "__main__":
    main()