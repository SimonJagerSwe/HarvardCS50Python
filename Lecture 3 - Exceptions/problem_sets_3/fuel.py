import math

def main():
    percent = get_fuel('Fraction: ')

    if percent <= 1 :
        print('E')
    elif percent >= 99:
        print('F')
    else:
        print(f'{round(int(percent))}%')


def get_fuel(fuel):
    while True:
        try:
            fraction = str(input('Fraction: '))
            split_fraction = fraction.split('/')
            x = int(split_fraction[0])
            y = int(split_fraction[-1])
            decimal = round(float(x / y) * 100)
            if x > y:
                pass
            elif y == 0:
                return ZeroDivisionError
            else:
                return decimal
        except:
            pass

main()
