########## STUDENT 2 ##########

# Example 1, implementing classes
'''
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    # student = Student()
    name = input("Name: ")
    house = input("House: ")
    # student = Student(name, house)
    # return student
    return Student(name, house)
'''


# Example 2, also validating user input
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    # student = Student()
    name = input("Name: ")
    house = input("House: ")
    # student = Student(name, house)
    # return student
    return Student(name, house)




if __name__ == "__main__":
    main()