########## EMAIL VALIDATOR ##########
import re
email = input("What's your email? ").strip()

#           - re.search(pattern, string, flags=)
# .         - any character except a newline
# *         - 0 or more repetitions
# +         - 1 or more repetitions
# ?         - 0 or 1 repetition
# {m}       - m repetitions
# {m, n}    - m-n repetitions
# ^         - matches the start of the string
# $         - matches the end of the string, just before the newline
# []        - set of characters
# [^]       - complementing the set
# \d        - decimal digit
# \D        - not a decimal digit
# \s        - whitespace characters
# \S        - not a whitespace character
# \w        - word character, includes alphabet, numerics and underscor, replaces [a-zA-Z0-9_]
# \W        - not a word character
# |         - or operator, allows several arguments in one place
# (...)     - a group
# (?:...)   - non-capturing version


# Example 1, no regex
'''if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")'''


# Example 2, still no regex, but better for validation
'''username, domain = email.split("@")

if username and "." in domain:      # If looking for a specific domain, use in domain.endswith("domain_name")
    print("Valid")
else:
    print("Invalid")'''


# Example 3, using regex, still not doing a good job
'''if re.search("@", email):
    print("Valid")
else:
    print("Invalid")'''


# Example 4, using regex, being more precise
'''if re.search(".*@.*", email):   # Will accept invalid input due to * accepting nothing as input
    print("Valid")
else:
    print("Invalid")'''

'''if re.search(".+@.+", email):   # Instead of .+ one can use ..*
    print("Valid")
else:
    print("Invalid")'''

# if re.search(r".+@.+\.edu", email):  # Backslash tells the program to look for the dot, not any character, needs to be formatted as a raw string
'''print("Valid")
else:
    print("Invalid")'''


# Example 5, looking for perfect match
# if re.search(r"^.+@.+\.edu$", email):        # Added extra backslash to escape backslash...
'''    print("Valid")
else:
    print("Invalid")
    '''

# if re.search(r"^[^@]+@[^@]+\.edu$", email):     # [^@] means any character EXCEPT @, preventing the adress from starting with an @, or using multiple @s in the middle
'''    print("Valid")
else:
    print("Invalid")'''

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):     # There's an easier way to do this. see below
'''    print("Valid")
else:
    print("Invalid")'''

# if re.search(r"^\w+@\w+\.edu$", email):
'''    print("Valid")
else:
    print("Invalid")'''

# if re.search(r"^\w+@\\w+\\.(com|edu|gov|net|org)$", email, re.IGNORECASE):   # If you want to allow spaces. instead of \w, use (\w|\s), not usable for email adresses
'''
    print("Valid")
else:
    print("Invalid")'''

# if re.search(r"^\w+@\w+\.\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):   # Allows you to also use extra dots for subdomains
'''    print("Valid")
else:
    print("Invalid")'''

# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
'''    print("Valid")
else:
    print("Invalid")'''

# if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):     # This allows dots to be used in the name as well as domain.
'''    # Possible alternative to (\w|\.) is [a-z0-9-\.]
    print("Valid")
else:
    print("Invalid")
'''

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
