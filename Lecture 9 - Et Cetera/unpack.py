# Example 1, only works with two names
'''
first, _ = input("What's your name? ").split(" ")
print(f"Hello, {first}")
'''


# Example 2
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]
coins = {"galleons" : 100, "sickles" : 50, "knuts" : 25}

# print(total(100, 50, 25), "Knuts")
# print(total(*coins), "Knuts")
print(total(**coins), "Knuts")
