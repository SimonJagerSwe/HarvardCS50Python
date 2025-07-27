########## STUDENT ##########

# Example 1, extremely basic
'''
def main():
    name = input("Name: ")
    house = input("House: ")
    print(f"{name} from {house}")
'''


# Example 2, more functional
'''
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")
'''


# Example 3, concentrating variables into one function that returns a tuple (immutable)
'''
def main():
    # name = get_name()
    # house = get_house()
    # name, house = get_student()
    student = get_student()
    print(f"{student[0]} from {student[1]}")
    # print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)    # using parenthesis to clarify that what is returned is one tuple, not two values (optional)
'''


# Example 4, using a list instead of a tuple, making it mutable
'''
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]    # Square brackets forces the program to return name and house as items in a list
'''

# Example 5, using dictionaries as using list index is tricky when many variables are used

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")     # Curreny Python supports using double quotes like this, older versions don't, so use with care

def get_student():
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student
    name = input("Name: ")
    house = input("House: ")
    return {"name" : name, "house" : house}     # This renders the student dict useless



if __name__ == "__main__":
    main()