########## CSV STUDENTS ##########
# # Example 1 
'''with open("students.csv") as file:
    for line in file:
        # row = line.rstrip().split(",")
        # print(f"{row[0]} is in {row[1]}")
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")'''


# Example 2, to help sorting
'''students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)'''


# Example 3
'''students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")'''


# Example 4, shorter than 3
'''students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")'''


# Example 5, more than two lines per row, using the csv module
'''import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        # students.append({"name" : row[0], "home" : row[1]})
        students.append({"name" : name, "home" : home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")'''


# Example 6, not using csv reader
'''import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name" : row["name"], "home" : row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")'''


# Example 7, writing to csv using csv writer
'''import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students_2.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])'''


# Example 8, writing to csv using dict writer
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open ("students_2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name" : name, "home" : home})