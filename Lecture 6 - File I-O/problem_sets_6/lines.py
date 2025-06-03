import os
import sys

valid_lines = []

def main():
    args = sys.argv
    check_input(args)
    file = args[1]
    # print(file)
    count_lines(file)
    # print(valid_lines)
    print(len(valid_lines))

def check_input(args):
    # print(args)
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    else:
        is_py = args[1] 
        if is_py[-3:] != ".py":
            sys.exit("Not a Python file")
        else:
            # print(args)
            if os.path.isfile(args[1]) == False:
                sys.exit("File does not exist")
        
            else:
                return args

def count_lines(file):
    with open(f"{file}") as file:
        # print(file)
            
        for line in file:            
            line = line.strip()
            print(line[slice(1)])
            # print(line)
            # print(f"{len(line)}")
            # print(type(line))
            # print(line[0])
            # print(line)
            # print(type(line))
            # print(line[0])
            if (
                # line[0] == "\n" or
                line == "\n" or
                line[slice(1)] == "#" or
                len(line) < 1
                ):
                # print(f"skipping line: {line}")
                pass

            else:
                # print(f"Appending line: {line}")
                valid_lines.append(line)

        return valid_lines

if __name__ == "__main__":
    main()