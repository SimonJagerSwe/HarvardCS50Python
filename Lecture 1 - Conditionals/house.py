########## HOUSE ##########
name = input('What\'s your name? ')

# This is way too long
'''
if name == 'Harry':
    print('Gryffindor')
elif name == 'Hermione':
    print('Gryffindor')
elif name == 'Ron':
    print('Gryffindor')
elif name == 'Draco':
    print('Slytherin')
else:
    print('Who?')
'''


# Better
'''
if name == 'Harry' or name == 'Hermione' or name == 'Ron':
    print('Gryffindor')
elif name == 'Draco':
    print('Slytherin')
elif:
    print('Who?')
'''


# Long case version
'''
match name:
    case 'Harry':
        print('Gryffindor')
    case 'Hermione':
        print('Gryffindor')
    case 'Ron':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Who?')
'''
# Short case version
match name:
    case 'Harry' | 'Hermione' | 'Ron':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Who?')
