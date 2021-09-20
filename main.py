def encode(key, text):
    result = ''
    stored = []
    i = 0
    while i < key:
        line = ''
        j = i + 0
        while j < len(text):
            line += text[j]
            j += key
        stored.append(line)
        i += 1
    k = 0
    while k < key:
        result += stored[k] + '\n'
        k += 1
    return result

key = int(input('Key? '))
text = input('Text? ')
print(encode(key, text))
input('Press any key to exit')
            
