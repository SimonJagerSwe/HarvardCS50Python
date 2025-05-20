import random

def main():
    guess_counter = 3
    answer = "" 
    get_level()
    generate_integer(get_level)
    print("Problems generated")
    '''temp = generate_integer(level)
    print(temp)
    temp_2 = temp(get_level)
    print(temp_2)'''
    
    


def get_level():
    print("Initialising get level")
    while True:
        try:
            level = input("Level: ")
            if level == "1" or level == "2" or level == "3":
                print("Level correct")                
            else:
                print("Incorrect level")
                continue

        except ValueError:
            continue

        return level
        # generate_integer(level)
        break
    

def generate_integer(level):
    print("Initialising integer generation")
    int_list = []
    problem_list = []
    
    for int in range(10):        
        if level == "1":
            integer = random.randint(0, 9)
            int_list.append(integer)
            # print(integer)
        elif level == "2":
            integer = random.randint(10, 99)
            int_list.append(integer)
            # print(integer)
        else:
            integer = random.randint(100, 999)
            int_list.append(integer)
            # print(integer)
     
    # print(integer)        
    print(int_list)

    for i in range(10):
        x = random.choice(int_list)
        print(x)
        y = random.choice(int_list)
        print(y)
        problem = x + y
        print(problem)
        problem_list.append([x, y, problem])
        # return problem
    
    print(problem_list)
    return problem_list

if __name__ == "__main__":
    main()