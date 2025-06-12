# Imports
import re
import sys


# Main function
def main():
    print(validate(input("IPv4 Address: ")))


# Validation function
def validate(ip):
    # print(type(ip))
    element_list = []
    # Split IP
    ip = ip.split(".")

    # Check IP length
    if len(ip) != 4:
        return False

    
    # Convert str to int
    for element in ip:        
        element = int(element)
        element_list.append(element)
        # print(element)
        # print(type(element))

    # print(element_list)        

    # Validate each element
    for element in element_list:
        #print(element)
         #print(type(element))
        if element >= 0 and element <= 255:
            continue            
        else:
            return False
        
    return True
    
    

    # return ip

if __name__ == "__main__":
    main()