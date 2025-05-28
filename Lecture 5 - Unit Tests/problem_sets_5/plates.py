def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    num_list = []
    banned_chars = [' ', ',', '.']


    if s[:2].isalpha() == False:
        return False

    elif len(s) < 2 or len(s) > 6:
        return False

    elif s[-1].isalpha() == True:
        for char in s:
            if char.isnumeric() == True:
                return False

    elif s[-1].isnumeric() == True:
        if s[-2].isalpha() == True:
            return False

    for char in s:
            if char.isnumeric() == True:
                num_list.append(char)
                if num_list[0] == '0':
                    return False

    for char in s:
        if char in banned_chars:
            return False


    else:
        return True

if __name__ == "__main__":
    main()
