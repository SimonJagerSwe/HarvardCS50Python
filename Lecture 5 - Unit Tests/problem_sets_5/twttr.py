def main():
    word = str(input('Input: '))
    print(shorten(word))


def shorten(word):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    # print(word)
    for char in word:
        # print(char)
        if char in vowels:
            word = word.replace(char, '')
    return word


if __name__ == "__main__":
    main()
