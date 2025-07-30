########## STUDENT 5 ##########

# Example 1, using @classmethod to put get function within the Student class 
# Better practice to place the main function at the top
def main():
    student = Student.get()
    print(student)


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    

# This function is made reduntant, and clarity is added to the program, as all methods and functions related to students are located within the Student class
'''
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
'''


if __name__ == "__main__":
    main()