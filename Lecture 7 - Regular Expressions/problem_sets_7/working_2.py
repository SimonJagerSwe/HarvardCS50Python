import re

def main():
    print(time_conversion(input("Hours: ")))

def time_conversion(s):
    # For first time, check if there are minutes present, if minutes are present, check that minutes are double digits, then find AM or PM, then repeat
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)

    # Check if time conforms to expressions
    if time:
        # Check that minutes don't exceed 59
        if time.group(2):
            if int(time.group(2)) >= 60:
                raise ValueError
            if int(time.group(5)) >= 60:
                raise ValueError
            
        # Evaluate starting hour
        starting_hour = int(time.group(1))
            
    #  If time format doesn't align with expressions, raise value error
    else:        
        raise ValueError


if __name__ == "__main__":
    main()