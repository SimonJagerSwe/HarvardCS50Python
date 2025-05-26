problem_list = [[1, 1, 2], [1, 2, 3], [2, 1, 3], [2, 2, 4], [3, 1, 4], [3, 2, 5], [3, 3, 6], [4, 1, 5], [4, 2, 6], [4, 3, 7]]
guess_counter = 3
score = 0

# while guess_counter
for item in problem_list:
    guess_counter = 3
    # print(item)
    x = item[0]
    y = item[1]
    z = item[2]
    print(x, y, z)
    guess = int(input(f"{x} + {y} = "))
    guess_counter -= 1
    print(guess)
    # if guess == z:
    #     print("Correct!")
    # else:
    #     print("Wrongo!")

    while True:
        while guess != z:
            # print(f"Guesses left {guess_counter}")
            print("EEE")
            guess = int(input(f"{x} + {y} = "))
            guess_counter -= 1
            # print(guess_counter)
            if guess_counter == 0:
                print(z)
                break
        if guess == z:
            score += 1
            break
        else:
            break
        
    print(f"Score: {score}")
