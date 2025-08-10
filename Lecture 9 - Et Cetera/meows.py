# Example 1, hard-coding the 3
'''
MEOWS = 3
for i in range(MEOWS):
    print("meow")
'''

# Example 2, using class variables
'''
class Cat:
    MEOWS = 3
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()
'''

# Example 3, adding type hints, allowing for mypy usage
'''def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
# meow(number)
meows: str = meow(number)
print(meows)
'''

# Example 4, more concise, and adding docstrings
def meow(n: int) -> str:
    """Meow n times."""     # This is a docstring
    """
    Meow n times.           # Alternate docstring style
    :param n: Number of times to meow
    :type n: int
    :raise TypeError:
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")