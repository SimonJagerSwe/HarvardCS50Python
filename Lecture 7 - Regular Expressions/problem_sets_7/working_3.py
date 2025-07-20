import re

def main():
    print(time_conversion(input("Hours: ")))


def time_conversion(s):
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)

    if time:
        if time.group(2):
            if int(time.group(2)) >= 60:
                raise ValueError("Can't have that many minutes, now can, we?")


    else:
        raise ValueError("Wrongo!!!")


if __name__ == "__main__":
    main()