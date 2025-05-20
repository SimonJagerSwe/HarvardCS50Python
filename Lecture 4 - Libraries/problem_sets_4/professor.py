import random


def main():
    print("Intitialising program")
    int_list = generate_integer(level=get_level())
    # guess_counter = 3
    # answer = "" 
    # problems = generate_integer(get_level)
    print("Main fetching integer list")
    # int_list = generate_integer(level=get_level())
    # int_list = generate_integer(int_list)
    print("Integers generated:")
    print(int_list)


def get_level():
    print("Initialising get level")
    while True:
        try:
            level = input("Level: ")
            if level == "1" or level == "2" or level == "3":
                print("Level correct")
                print(f"Level: {level}")
            else:
                print("Incorrect level")
                continue

        except ValueError:
            continue

        print(f"Returning level: {level}")
        return level
        # generate_integer(level)
        # break
    

def generate_integer(level):
    print(f"Initialising integer generation with level: {level}")
    int_list = []
    # problem_list = []
        
    if level == "1":
        for int in range(10):
            integer = random.randint(0, 9)
            int_list.append(integer)
            print(f"Adding single digit integer {integer}")
    elif level == "2":
        for int in range(10):
            integer = random.randint(10, 99)
            int_list.append(integer)
            print(f"Adding double digit integer {integer}")
    elif level == "3":
        for int in range(10):
            integer = random.randint(100, 999)
            int_list.append(integer)
            print(f"Adding triple digit integer {integer}")
    else:
        print("[ERROR]")
        
     
    print(int_list)
    return int_list

    '''for i in range(10):
        x = random.choice(int_list)
        print(f"x = {x}")
        y = random.choice(int_list)
        print(f"y = {y}")
        problem = x + y
        print(f"problem: {x} + {y} = {problem}")
        problem_list.append([x, y, problem])
    
    print(problem_list)
    print(type(problem_list))
    print("Returning problem list")
    return problem_list'''

if __name__ == "__main__":
    main()