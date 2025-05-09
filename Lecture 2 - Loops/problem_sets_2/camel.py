camelCase = str(input('camelCase: '))
snake_string = ''

if camelCase.islower() == True:
    print(camelCase)

else:
    for char in camelCase:
        if char.isupper() == True:
            camelCase = camelCase.replace(char, ('_' + char.lower()))
    print(camelCase)
