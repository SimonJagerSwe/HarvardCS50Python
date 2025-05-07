########## COMMAND LINE INPUT ##########
import sys


# First example, will crash gently
'''try:
    print("Hello, my name is", sys.argv[1])

except IndexError:
    print("Too few arguments!")'''


# Second example, also crashes gently, but more clearly, has no error handling
'''if len(sys.argv) < 2:
    print("Too few arguments")

elif len(sys.argv) > 2:
    print("Too many arguments!")
else:
    print("Hello, my name is", sys.argv[1])'''


# Third example, exits without raising errors, while being clearer than using else to print the desired string
'''if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])'''


# Fourth example, taking more than one argument
if len(sys.argv) < 2:
    sys.exit("Too few arguments!")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)