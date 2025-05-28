def main():
    greeting = str(input("Greeting: ")).lower().strip()
    print(value(greeting))


def value(greeting):
    if greeting.lower().strip()[0] != "h":
        return 100

    elif greeting.lower().strip()[:5] == "hello":
        return 0

    else:
        return 20


if __name__ == "__main__":
    main()
