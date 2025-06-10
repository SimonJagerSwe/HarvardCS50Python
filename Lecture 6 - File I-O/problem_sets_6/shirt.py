# Imports
import os
import sys

from PIL import Image


# Main function
def main():
    # Take arguments
    arguments = sys.argv
    verify_args(arguments)
    # print(arguments)
    file_1 = arguments[1]
    print(file_1)
    file_2 = arguments[2]
    print(file_2)
    handle_images(file_1, file_2)



# Verify arguments function
def verify_args(args):
    file_formats = ["png", "jpg", "jpeg"]

    # Verify number of arguments
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    if len(args) > 3:
        sys.exit("Too many command-line arguments")

    # Verify input file
    if os.path.isfile(args[1]) == False:
        sys.exit("Input file not found")

    # Identify file format
    input_file_format = str(args[1]).lower().split(".")
    output_file_format = str(args[2]).lower().split(".")
    # print(args)

    # Verify file format
    if (input_file_format[-1] not in file_formats):
        sys.exit("Invalid input")    
    if (output_file_format[-1] not in file_formats):
        sys.exit("Invalid input")    
    if output_file_format[-1] != input_file_format[-1]:
        sys.exit("Input and output have different extensions")

    
# Image handling
def handle_images(file_1, file_2):
    pass

# File execution check
if __name__ == "__main__":
    main()