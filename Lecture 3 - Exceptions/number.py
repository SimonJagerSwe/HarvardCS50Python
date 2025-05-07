########## NUMBER ##########
def main():
    x = get_int('What\'s x? ')
    print(f'x is {x}')


def get_int(prompt):
    while True:
        try: 
            # x = int(input('What\'s x? '))
            # print(f'x is {x}')            NOT IDEAL TO KEEP PRINT WITHIN TRY
            return int(input(prompt))
        except ValueError:
            # print('x is not an integer!')
            pass
        # print(f'x is {x}')                WILL CAUSE NameError
#         else:        
#            return x
    
    
main()