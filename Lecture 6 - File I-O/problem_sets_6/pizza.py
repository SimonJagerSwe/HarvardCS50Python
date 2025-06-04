# Imports
import csv
import sys

from tabulate import tabulate

# Main function
def main():

    # Get file name
    args = sys.argv
    csv_file = validate_input(args)[1]
    # print(file)
    print(handle_file(csv_file))


# Validate input
def validate_input(args):
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    if len(args) > 2:
        sys.exit("Too many command-line arguments")
    else:
        # print(args[1])
        arg_type = args[1][-4:]
        # print(arg_type)
        if arg_type != ".csv":
            sys.exit("Not a CSV file")
        else:
            return args


# File handling
def handle_file(csv_file):
    line_list = []
    # header = []
    # body = []
    
    with open(f"{csv_file}") as file:
        reader = csv.reader(file)
        print(reader)
        # print(file)
        # print(tabulate(file))
        for line in reader:
            # print()
            line_list.append(line)
        
        print(line_list)
        # header = line_list[0]
        # print(header)
        # body = line_list[1:]
        # print(body)
        # table = [[header], body]
        # print(tabulate(table))
        # print(tabulate(body, headers=[header]))
        return tabulate(line_list, headers="firstrow", tablefmt="grid")

if __name__ == "__main__":
    main()