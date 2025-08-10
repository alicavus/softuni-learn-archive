secret_msg = input().split()

message = []

for word in secret_msg:
    ascii_code = ''
    for idx, character in enumerate(word):
        if character.isdigit():
            ascii_code += character
        else:
            word = chr(int(ascii_code)) + word[idx:]
            break

    if len(word) > 2:
        word = word[0] + word[-1] + word[2:len(word)-1] + word[1]

    message += [word]

print(" ".join(message))



