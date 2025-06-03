import sys

def main():
    valid_lines = []

    if len(sys.argv) == 2:
        # print("Yeeeaah")
        file_name = sys.argv[1]
        if file_name[-3:] != ".py":
            sys.exit("Not a Python file")
        else:
            # print("Yeeeaah")
            with open(f"{file_name}") as file:
                print(file)
            
                for line in file:
                    print(line)
                    if line[0] == "#" or line[0] == "\n":
                        pass
                    else:
                        valid_lines.append(line)
            
            print(valid_lines)
            print(len(valid_lines))


    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    else:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()