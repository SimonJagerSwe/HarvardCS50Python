########## RANDOM GENERATION ##########
# First example, coin flip 1
'''import random

# print(random.choice(["heads", "tails"]))
coin = random.choice(["heads", "tails"])
print(coin)'''


# Second example, coin flip 2
'''from random import choice

coin = choice(["heads", "tails"])
print(coin)'''


# Third example, random integer
'''import random

number = random.randint(1, 10)
print(number)'''


# Fourth example, shuffle
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)