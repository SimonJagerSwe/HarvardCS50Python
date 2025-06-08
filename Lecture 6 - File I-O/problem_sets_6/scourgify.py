# Imports
import csv
import os
import sys
# students = {}



# Main function
def main():
    args = sys.argv    
    arguments = verify_input(args)
    # print(arguments)
    file_1 = arguments[1]
    file_2 = arguments[2]
    # print(file_name)
    read_file(file_1, file_2)
    # extract_names(file_name)
    # print(correct_list)
    # reverse_names(name_list)
    # print(new_dict)
    # print(students)
    # print(student_list)


# Verify input function
def verify_input(args):
    # print(args)
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    elif os.path.isfile(args[1]) == False:
            sys.exit(f"Could not read {args[1]}")
    else:
        file_format = args[1][-4:]
        file_format_2 = args[2][-4:]
        # print(file_format)
        if file_format != ".csv" and file_format_2 != ".csv":
            sys.exit("Not a CSV file")
        else:
            return args


# Create new list from old file
def read_file(file_1, file_2):
    student_list = []
    # print(file_1, file_2)
    with open(f"{file_1}") as file:
        reader = csv.DictReader(file)
        for line in reader:
            # print(line)
            name = line["name"].split(",")
            # print(f"{name[1]} {name[0]} {line["house"]}")
            student_first_name = name[1].strip()
            student_last_name = name[0].strip()
            student_house = line["house"].strip()
            student_info = student_first_name, student_last_name, student_house
            # print(student_info)
            # print(student_name, line["house"])
            # new_dict.update("name" : student_name, "house" : )
            # print(student_first_name, student_last_name, student_house)
            # students.update({"first" : student_first_name, "last" : student_last_name, "house" : student_house})
            student_list.append(student_info)

        with open(f"{file_2}", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for student in student_list:
                    writer.writerow({"first" : student[0], "last" : student[1], "house" : student[2]})



if __name__ == "__main__":
    main()