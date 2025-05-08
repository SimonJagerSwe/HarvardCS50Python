greeting = str(input("Greeting: ")).lower().strip()

if greeting[0] != "h":
    print("$100")

elif greeting[:5] == "hello":
    print("$0")

else:
    print("$20")
