# Imports
import os
import sys

from PIL import Image
from PIL import ImageOps


# Main function
def main():
    # Take arguments
    arguments = sys.argv
    verify_args(arguments)
    # print(arguments)
    before = arguments[1]
    # print(before)
    shirt = "shirt.png"
    # print(shirt)
    after = arguments[2]
    # print(after)
    handle_images(before, shirt, after)



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
def handle_images(muppet, shirt, after):
    muppet = Image.open(muppet)
    shirt = Image.open(shirt)    
    # print(muppet.size, shirt.size)
    muppet = ImageOps.fit(muppet, [shirt.size[0], shirt.size[1]])
    # shirt = ImageOps.fit(shirt, [900, 1200])  # size=[muppet.size[0], muppet.size[1]]
    # print(shirt.size)
    muppet.paste(shirt, (0, 0), mask = shirt)

    # muppet.show()
    muppet.save(after)

# File execution check
if __name__ == "__main__":
    main()