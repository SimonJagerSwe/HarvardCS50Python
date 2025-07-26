import validator_collection

def main():
    print(validator(input("What's your email adress? ")))


def validator(s):
    check_email = validator_collection.is_email(s)

    if check_email:
        return "Valid"
    else:
        return "Invalid"
    
    
if __name__ == "__main__":
    main()