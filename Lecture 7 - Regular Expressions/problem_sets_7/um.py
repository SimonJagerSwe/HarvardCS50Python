import re

def main():
    print(count(input("Text: ").lower()))


def count(s):
    counter = 0
    delimiters = [",", "."]
    new_string = ""
    # temp_list = []
    # words = .split(delimiters, s)
    # return words
    for char in s:
        if char in delimiters:
            # temp_list.append(char)
            new_string.append(s.replace(char, " ").split(" "))
        print(new_string)

    for word in new_string:
        if word == "um":
            counter += 1

    return f"The string \"{s}\" contains {counter} of ums"


    # return new_string
    # return new_string
    '''for word in words:
        if word == "um":
            counter += 1
    
    return counter'''


if __name__ == "__main__":
    main()