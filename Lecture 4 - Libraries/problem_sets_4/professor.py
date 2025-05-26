import random


def main():
    problem_list = []    
    score = 0
    guess_counter = 3

    integer = generate_integer(level=get_level())
    print(f"Integers: {integer}")
    # int_list
    print("Generating problems..")

    # for i in range(10):
        # x = random.choice(int_list)
        # y = random.choice(int_list)
        # problem = x + y
        # problem_list.append([x, y, problem])
    
    print(f"Problem list:")
    print(problem_list)

       
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
    print("Initialising get level...")
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
    int_list = []
 
    if level == "1":
        for int in range(10):
            integer = random.randint(0, 9)                    
            # int_list.append(integer)
            # return integer
    elif level == "2":
        for int in range(10):
            integer = random.randint(10, 99)
            # int_list.append(integer)
            # return integer
    else:
        for int in range(10):
            integer = random.randint(100, 999)
            # int_list.append(integer)
            # return integer

    # print(int_list)
    # return int_list
    return integer

if __name__ == "__main__":
    main()