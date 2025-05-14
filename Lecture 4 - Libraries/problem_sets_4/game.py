# Imports
import random

# Validate level input
while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            level = int(input("Level: "))
        break

    except:
        continue

# Generate number
number = random.randint(1, level)

# Validate guess input
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            guess = int(input("Guess: "))
        elif guess > level:
            guess = int(input("Too large!"))
            continue
        break

    except:
        continue

# Compare guess to generated number
while True:
    if guess < number:
        print("Too small!")
        guess = int(input("Guess: "))

    elif guess > number:
        print("Too large!")
        guess = int(input("Guess: "))

    else:
        print("Just right!")
        break
