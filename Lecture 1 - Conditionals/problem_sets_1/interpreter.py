expression = input("Expression: ")

def main():
    if "+" in expression:
        split_expression = expression.split("+")
        x = split_expression[0]
        y = split_expression[1]
        print(add(x, y))

    
    elif "-" in expression:
        split_expression = expression.split("-")
        x = split_expression[0]
        y = split_expression[1]
        print(sub(x, y))


    elif "*" in expression:
        split_expression = expression.split("*")
        x = split_expression[0]
        y = split_expression[1]
        print(mul(x, y))


    elif "/" in expression:
        split_expression = expression.split("/")
        x = split_expression[0]
        y = split_expression[1]
        print(div(x, y))


def add(x, z):
    return float(int(x) + int(z))

def sub(x, z):
    return float(int(x) - int(z))

def mul(x, z):
    return float(int(x) * int(z))

def div(x, z):
    return float(int(x) / int(z))

main()
