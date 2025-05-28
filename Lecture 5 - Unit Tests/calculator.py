# Simple function to test squared
def main():
    # x = int(input("What's x? "))  # Correct method to ensure integer input
    x = input("What's x? ")     # Introducing an error
    print("x squared is", square(x))

def square(n):
    return n*n    # Correct method for a squaring function
    # return n + n    # Introducing an error

if __name__ == "__main__":
    main()