# Main function, takes input, sends to validation function, sends valid input to conver function
def main():
    s = validate_input(input("Hours: "))
    print(s)
    print(convert(s))


# Convert function
def convert(s):
    start, stop = s.split("to")
    # return start, stop

    # Check for minutes, if no minutes are present, add ":00"
    if not ":" in start:
        start = f"{start}:00"
    if not ":" in stop:
        stop = f"{stop}:00"
    return start, stop

    # Check if start is in AM or PM

    # Check if stop is in AM or PM


# Input validation
def validate_input(s):
    # Check if "to" is used in s, if not, returns an error
    if not "to" in s:
        return ValueError("Invalid time format")
    
    # Create two times for validation
    start, stop = s.split("to")

    # Split first time in hours and minutes
    if ":" in start:
        start_h, start_m = start.split(":")
        start_m = start_m.split(" ")[0]
        start_h, start_m = int(start_h), int(start_m)

    # Split second time in hours and minutes
    if ":" in stop:
        stop_h, stop_m = stop.split(":")
        stop_m = stop_m.split(" ")[0]
        stop_h, stop_m = int(stop_h), int(stop_m)

    # Validate that there are no more than 12 hours or 59 minutes, and that no negative numnbers are used, return an error if format is not valid   
    if (
        start_h > 12 or 
        start_h < 0 or
        start_m > 59 or
        start_m < 0 or
        stop_h > 12 or
        stop_h < 0 or
        stop_m > 59 or
        stop_m < 0
        ):
        return ValueError("Invalid time format")
        
    
    # Return a valid number to be used for conversion
    return s    

# Execute main function
if __name__ == "__main__":
    main()