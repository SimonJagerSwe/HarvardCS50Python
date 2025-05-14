# Imports
import sys

from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()
# print(font_list)
'''f = "slant"
s = "Hello, World!"

# print(figlet.getFonts())
figlet.setFont(font=f)
print(figlet.renderText(s))'''

# Input
'''str = str(input("Input: "))
if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid number of arguments :(")
'''
# Evaluate input
# If zero input arguments
if len(sys.argv) == 1:
    str = str(input("Input: "))
    print(len(sys.argv))
    print(figlet.renderText(str))

# If two input arguments
elif len(sys.argv) == 3:    
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":        
        f = sys.argv[2]
        if f in font_list:
            str = str(input("Input: "))
            print(f)
            figlet.setFont(font=f)
            print(figlet.renderText(str))
        else:
            sys.exit("Invalid command line argument :(")

    else:        
        sys.exit("Invalid command line argument :(")

# If other amount of input arguments
else:
    sys.exit("Invalid number of arguments :(")
# Output result
