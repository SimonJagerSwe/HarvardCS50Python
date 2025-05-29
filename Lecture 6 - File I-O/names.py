########## NAMES ##########
# Example 1
'''names = []

for _ in range(3):    
    # name = input("What's your name? ")
    # names. append
    names.append(input("What's your name? "))   # Shorter than the two lines above


for name in sorted(names):
    print(f"Hello, {name}")


# print(f"Hello, {name}")
# print(names)'''


# Example 2, not using with
'''name = input("What's your name? ")

# file = open("names.txt", "w")   # "w" will overwrite everything in the file every time
file = open("names.txt", "a")   # "a" will append to file
# file.write(name)    # This doesn't add any spaces or line breaks to the file
file.write(f"{name}\n")
file.close()    # Forgetting this causes memory leaks or can lead to accidental overwriting'''


# Example 3, using with, which automatically closes the file to prevent memory leaks
# name = input("What's your name? ")

'''with open("names.txt", "a") as file:
    file.write(f"{name}\n")'''

# with open("names.txt", "r") as file:      # These lines will print with an extra line break
#     lines = file.readlines()
# for line in lines:            
#     print(f"Hello, {line}")

# with open("names.txt", "r") as file:      # Not ideal, can't sort
#     for line in file:
#         print("Hello,", line.rstrip())

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")