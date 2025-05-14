# Imports
import inflect
p = inflect.engine()

name_list = []

while True:
    try:
        name = str(input("Name: "))
        name_list.append(name)
        output = f"Adieu, adieu, to {p.join(name_list)}"

    except EOFError:
        print(output)
        break
