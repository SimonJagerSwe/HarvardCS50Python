def main():
    total = float(0)
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    while True:
        try:
            item = input("Item: ").title()
            if item in menu:
                price = menu[item]
                total += price

            else:
                item = input("Item: ").title()

        except KeyboardInterrupt as ki:
            print(f"${total:.2f}")
            print(f"Caught: {ki}")
            print("Program terminated")
            break

        except EOFError:
            print(f"${total:.2f}.")
            print("Program terminated!")
            break


        print(f"${total:.2f}")


main()
