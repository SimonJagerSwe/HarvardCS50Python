import random
random.seed(500)


def main():
    problem_list = []
    score = 0

    level = get_level()

    for integer in range(10):
        x = generate_integer(level)
        # print(x)
        y = generate_integer(level)
        # print(y)
        answer = x + y
        print(f"{x} + {y}")
        print(f"Answer: {answer}")
        problem_list.append([x, y, answer])

    # print(problem_list)
    for question in problem_list:
        guess_counter = 3
        question_x = question[0]
        question_y = question[1]
        answer = question[2]
        guess = int(input(f"{question_x} + {question_y} = "))
        guess_counter -= 1

        while True:
            while guess != answer:
                print("EEE")
                guess = int(input(f"{question_x} + {question_y} = "))
                guess_counter -= 1

                if guess_counter == 0:
                    print(answer)
                    break

            if guess == answer:
                score += 1
                break
            else:
                break

        print(score)


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
