########## COMPARE ##########
x = int(input('What is x? '))
y = int(input('What is y? '))


# Not good programing, and inefficient 
'''
if x < y:
    print('x is less than y')

if x > y:
    print('x is greater than y')

if x == y:
    print('x is equal to y')
'''

# Better
if x < y:
    print('x is less than y')

elif x > y:
    print('x is greater than y')

else:
    print('x is equal to y')


# Equal or not v.1
'''
if x < y or x > y:
    print ('x is not equal to y')

else:
    print('x is equal to y')
'''


# Equal or not v.2
if x != y:
    print('x is not equal to y')
else:
    print('x is equal to y')