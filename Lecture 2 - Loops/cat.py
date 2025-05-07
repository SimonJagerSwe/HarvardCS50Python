########## CAT ##########
# Useless version
'''
print('Meow')
print('Meow')
print('Meow')
'''

# Bad version using loops, will create an infinite loops
'''
i = 3
while i != 0:
    print('Meow')

# Functional version using loops
i = 0
while i < 3:
    print('Meow')
    i += 1

print('\n')

# Using for loop and list:
for i in [0, 1, 2]:
    print('Meow')

print('\n')

# Better and cleaner:
for i in range(30):
    print('Meow')

print('\n')

# Another version
print('meow\n' * 3, end = '')

print('\n')

# Ask the user for number of meows
while True:
    n = int(input('What\'s n? '))
    if n > 0:
        break

for _ in range(n):
    print('Meow')
'''    

# Using functions
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input('What\'s n? '))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print('meow')

main()