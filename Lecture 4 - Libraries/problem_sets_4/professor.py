import random


def main():
    problem_list = []    
    correct_answers = 0

    int_list = generate_integer(level=get_level())
    print("Generating problems..")

    for i in range(10):
        x = random.choice(int_list)
        y = random.choice(int_list)
        problem = x + y
        problem_list.append([x, y, problem])
    
    print(f"Problem list:")
    print(problem_list)

    while len(problem_list) > 0:
        guess_counter = 3
        for question in problem_list:
            question_x = question[0]
            question_y = question[1]
            answer = question[2]
            guess = int(input(f"{question_x} + {question_y} = "))


            while guess_counter > 0:
                # guess = int(input(f"{question_x} + {question_y} = "))
                if guess == answer:
                    problem_list.remove(question)
                    print(problem_list)
                    correct_answers += 1
                    print(correct_answers)
                    break
                else:
                    print("EEE")
                    guess_counter -= 1
                    print(f"Number of guesses left: {guess_counter}")
                    # guess = int(input(f"{question_x} + {question_y} = "))
                    continue
                print(f"{question_x} + {question_y} = {answer}")
            problem_list.remove(question)
            print(problem_list)
            # continue
            
    print(f"Score: {correct_answers}")


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
            int_list.append(integer)
    elif level == "2":
        for int in range(10):
            integer = random.randint(10, 99)
            int_list.append(integer)
    else:
        for int in range(10):
            integer = random.randint(100, 999)
            int_list.append(integer)

    print(int_list)
    return int_list

if __name__ == "__main__":
    main()