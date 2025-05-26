import random


def main():
    problem_list = []
    level = get_level()
    generate_integer(level)

    for integer in range(10):
        x = generate_integer(level)
        # print(x)
        y = generate_integer(level)
        # print(y)
        answer = x + y
        print(f"{x} + {y}")
        print(f"Answer: {answer}")


def get_level():
    while True:
        try:
            level = input("Level: ")
            if level == "1" or level == "2" or level == "3":
                level = level
            else:
                continue

        except ValueError:
            continue

        return level

def generate_integer(level):
    if level == "1":
        for int in range(10):
            integer = random.randint(0, 9)
    elif level == "2":
        for int in range(10):
            integer = random.randint(10, 99)
    else:
        for int in range(10):
            integer = random.randint(100, 999)

    return integer


if __name__ == "__main__":
    main()
