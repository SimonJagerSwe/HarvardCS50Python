import random


def main():
    get_level()
    guess_counter = 3
    answer = "" 
    


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

        generate_integer(level)
        break
    

def generate_integer(level):
    print("Initialising integer generation")
    int_list = []
    
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

if __name__ == "__main__":
    main()