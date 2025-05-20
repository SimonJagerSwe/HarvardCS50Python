import random


def main():
    problem_list = []    
    correct_answers = 0

    # print("Intitialising program...")
    int_list = generate_integer(level=get_level())    
    # print("Main fetching integer list...")
    # print("Integers generated:")
    # print(int_list)
    print("Generating problems..")

    for i in range(10):
        x = random.choice(int_list)
        # print(f"x = {x}")
        y = random.choice(int_list)
        # print(f"y = {y}")
        problem = x + y
        # print(f"problem: {x} + {y} = {problem}")
        problem_list.append([x, y, problem])
    
    print(f"Problem list:")
    print(problem_list)
    # print(type(problem_list))

    while len(problem_list) > 0:
        guess_counter = 3
        # print(random.choice(problem_list))
        # question = random.choice(problem_list)
        for question in problem_list:
            # print(question)
            question_x = question[0]
            # print(question_x)
            question_y = question[1]
            # print(question_y)
            answer = question[2]
            # print(answer)
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
    # print(answer)


def get_level():
    print("Initialising get level...")
    while True:
        try:
            level = input("Level: ")
            if level == "1" or level == "2" or level == "3":
                # print("Level correct")
                # print(f"Level: {level}")
                level = level
            else:
                # print("Incorrect level")
                continue

        except ValueError:
            continue

        # print(f"Returning level: {level}")
        return level
        # generate_integer(level)
        # break
    

def generate_integer(level):
    # print(f"Initialising integer generation with level: {level}")
    int_list = []
    # problem_list = []
        
    if level == "1":
        for int in range(10):
            integer = random.randint(0, 9)
            int_list.append(integer)
            # print(f"Adding single digit integer {integer}")
    elif level == "2":
        for int in range(10):
            integer = random.randint(10, 99)
            int_list.append(integer)
            # print(f"Adding double digit integer {integer}")
    else:
        for int in range(10):
            integer = random.randint(100, 999)
            int_list.append(integer)
            # print(f"Adding triple digit integer {integer}")
        
     
    print(int_list)
    return int_list

if __name__ == "__main__":
    main()