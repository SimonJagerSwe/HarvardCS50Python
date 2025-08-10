# Example 1
'''
def main():
    yell("This is CS50")

def yell(phrase):
    print(phrase.upper())


if __name__ == "__main__":
    main()
'''


# Example 2
'''
def main():
    # yell(["This", "is", "CS50"])
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

    
if __name__ == "__main__":
    main()
'''


# Example 3
'''
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
'''


# Example 4
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()