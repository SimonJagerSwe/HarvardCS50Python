import math

def main():
    fuel = str(input("Fraction: "))

    fractions = convert(fuel)
    print(fractions)
    # print(fractions[0])
    # print(fractions[1])

    decimal = round(float(fractions[0] / fractions[1]) * 100)
    # print(decimal)
    print(gauge(decimal))

def convert(fraction):
    split_fraction = fraction.split("/")
    x = int(split_fraction[0])
    y = int(split_fraction[-1])
    return x, y
    
    
def gauge(percentage):
    if percentage <= 1 :
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(int(percentage))}%"


if __name__ == "__main__":
    main()
