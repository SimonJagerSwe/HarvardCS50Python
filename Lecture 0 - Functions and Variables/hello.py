##### HELLO #####

# STEP 1
# print('Hello World!')
# print('Hello World!'      WILL THROW SYNTAX ERROR


# STEP 2
# Version 1, tedious
# print('What\'s your name?')
# input()

# Version 2, cleaner
# input('What\'s your name? ')
# print('Hello, David')       THIS IS IMUTABLE

# Version 3, using variable and two different ways of calling name, first one being old, second one being new and standard
# name = input('What\'s your name? ')
# print('Hello, ' + name + '!')
# print(f'Hello, {name}!')

# Futzing with endings
# print('Hello,', end = '')
# print(f' {name}')


# STEP 3
# Using quotes
# print('"Wow." Now I\'m using "quotation marks". That\'s "really cool"...')


# STEP 4
# Stripping and other functions
# name_1 = input('What\'s your name? ')
# name_1 = name_1.strip()
# print(f'Hello, {name_1}!')

# name_1 = name_1.capitalize()
# print(f'Hello, {name_1}!')

# name_1 = name_1.title()
# print(f'Hello, {name_1}!')

# name_1 = name_1.upper()
# print(f'Hello, {name_1}!')
 

##### USE FUNCTIONS #####
# STEP 1
# def hello():
#     name = input('What\'s your name? ')
#     return name
# print(hello())


# STEP 2
# def hello(to):
#     print('Hello', to)
# name = input('What\'s your name? ')
# hello(name)


# STEP 3
def main():
    name = input('What\'s your name? ')
    hello(name)


def hello(to = 'World'):
    print('Hello, ', to)

main()