string = str(input('Input: '))
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

for char in string:
    if char in vowels:
        string = string.replace(char, '')

print(string)
