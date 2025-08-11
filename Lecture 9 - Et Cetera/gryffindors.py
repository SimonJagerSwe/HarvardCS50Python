# Example 1
'''
students = [
    {"name" : "Hermione", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"}
]

gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]

for gryffindor in sorted(gryffindors):
    print(gryffindor)

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
'''

# Example 2
'''
students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name" : student, "house" : "Gryffindor"})

print(gryffindors)
'''

# Example 3
'''
students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name" : student, "house" : "Gryffindor"} for student in students]
print(gryffindors)
'''

# Example 4
'''
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student : "Gryffindor" for student in students}
print(gryffindors)
'''

# Example 5

students = ["Hermione", "Harry", "Ron"]
'''
# for i in range(len(students)):
    # print(i + 1, students[i])     # Better to enumerate to skip student index

for i, student in enumerate(students):
    print(i + 1, student)
'''

# Example 6, problematic for large loops
'''
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    # return "🐑" * n
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()
'''

# Example 7
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()