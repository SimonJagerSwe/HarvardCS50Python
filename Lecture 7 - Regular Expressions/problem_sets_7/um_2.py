import re

def main():
    print(count(input("Text: ")))


def count(s):
    # counter = 0
    # delimiters = [",", "."]
    new_s = re.sub(r"[,|.|?|!|;|\s+]", " ", s).lower()
    # return new_s
    split_s = new_s.split(" ")
    um_list = []    
    # print(split_s)
    # return split_s
    for word in split_s:
        if word == "um":
            um_list.append(word)

    return len(um_list)

if __name__ == "__main__":
    main()