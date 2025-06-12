import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # print(s)
    # print(type(s))
    # elements = re.search(r"^(?:<iframe.+)?src=https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)>?$", s, re.IGNORECASE)
    # elements = re.search(r"^(?:<iframe.+)src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)", s)
    # print(elements)
    # print(elements.group(1))
    

    if s := re.search(r"^(?:<iframe.+)?(?:src=)?\"?https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\".+>$", s):
    # print(s[0])
        # print(s.group(1))
        # id = s.group(1)
        # print(id)
        # short = f"https://youtu.be/{id}"
        # short = f"https://youtu.be/{s.group(1)}"
        # return short
        return f"https://youtu.be/{s.group(1)}"
    else:
        return None

    # return s


if __name__ == "__main__":
    main()