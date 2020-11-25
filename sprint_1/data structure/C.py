string= input()
result = 0

while len(string) != 0:
    intermediate = ''

    for letter in string:
        if letter not in intermediate:
            intermediate += letter
        else:
            if len(intermediate) > result:
                result = len(intermediate)
            string = string[string.index(letter) + 1:]
            break

    if intermediate == string:
        string = ''
        if len(intermediate) > result:
            result = len(intermediate)


print(result)
