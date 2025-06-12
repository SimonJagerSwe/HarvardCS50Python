########## FORMATTING USER INPUT ##########
import re
name = input("What's your name? ").strip()
# print(f"Hello, {name}!")

# Example 1, no regex
'''if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"Hello, {name}!")'''


# Example 2, using regex capturing
'''matches = re.search(r"^(.+), ?(.+)$", name)
if matches:
    last, first = matches.groups()
    # Alternative 1 is:
    # last = matches.group(1)
    # first = matches.group(2)
    # Alternative 2 is:
    # name = matches.group(2) + " " + matches.group(1)      # BUT WHY???
    name = f"{first} {last}"
print(f"Hello, {name}!")'''


# Example 3, BRING ON THE WALRUS
if matches := re.search(r"^(.+), *(.+)$", name):
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"Hello, {name}!")
