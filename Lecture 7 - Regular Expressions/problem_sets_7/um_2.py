import re

def main():
    print(count(input("Text: ").lower()))


def count(s):
    counter = 0
    # delimiters = [",", "."]
    new_s = re.sub(r"[ |,|.]", " ", s)
    # return new_s
    split_s = new_s.split(" ")
    # return split_s
    for word in split_s:
        if word == "um":
            counter += 1

    return counter    

if __name__ == "__main__":
    main()