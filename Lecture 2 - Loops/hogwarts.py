########## HOGWARTS ##########
# Less than ideal version
'''
students = ['Hermione', 'Harry', 'Ron', 'Draco']
houses = ['Gryffindor', 'Gryffindor', 'Gryffindor', 'Slytherin']


for student in students:
    print(student)


for i in range(len(students)):
    print(i + 1, students[i])
    '''

# Better to use dictionaries
'''
students = {
    'Hermione' : 'Gryffindor',
    'Harry' : 'Gryffindor',
    'Ron' : 'Gryffindor',
    'Draco' : 'Slytherin'
    }

# print(students)
print(students['Hermione'])
print(students['Harry'])
print(students['Ron'])
print(students['Draco'])

for student in students:
    print(student, students[student], sep = ', ')
'''

students = [
    {'name' : 'Hermione', 'house' : 'Gryffindor', 'patronus' : 'Otter'},
    {'name' : 'Harry', 'house' : 'Gryffindor', 'patronus' : 'Stag'},
    {'name': 'Ron', 'house' : 'Gryffindor', 'patronus' : 'Jack Russel terrier'},
    {'name' : 'Draco', 'house' : 'Slytherin', 'patronus' : None}
    ]

for student in students:
    print(student['name'], student['house'], student['patronus'], sep = ', ')