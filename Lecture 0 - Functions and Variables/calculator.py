##### CALCULATOR #####

# STEP 1
# x = 1
# y = 2
# z = x + y
# print(z)
 

# STEP 2                THIS WILL CONCATENATE AS DEFAULT INPUT IS STRING
# x = input('What\'s X? ')
# y = input('What\'s y? ')
# z = x + y
# print(z)
 

# STEP 3
# x = int(input('What\'s X? '))
# y = int(input('What\'s y? '))
# z = x + y
# print(z)


# STEP 4 - Rounding
 #print(round(12.3452342, 3))
# x = float(input('What\'s X? '))
# y = float(input('What\'s y? '))
# z = round(x + y)
# z_1 = round((x + y), 1)
# z_2 = round((x + y), 2)
# print(z)
# print(z_1)
# print(z_2)


# STEP 5
# x = float(input('What\'s x? '))
# y = float(input('What\'s y? '))
# z = x / y
# print(round(z))
# print(f'{z:.2f}')


# STEP 6
def main():
    x = int(input('What\'s x? '))    
    print('x squared is', square(x))

def square(n):
    return n * n
    

main()