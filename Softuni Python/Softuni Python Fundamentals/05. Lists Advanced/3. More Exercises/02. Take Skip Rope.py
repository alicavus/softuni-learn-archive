numbers_list = []
texts_list = []

for character in input():
    if character.isdigit():
        numbers_list += [int(character)]
    else:
        texts_list += [character]

take_list = numbers_list[::2]
skip_list = numbers_list[1::2]

final_string = []

while take_list or skip_list:
    if len(take_list):
        char_count = take_list.pop(0)
        final_string += texts_list[:char_count]
       
    texts_list = texts_list[char_count:]

    if len(skip_list):
        char_count = skip_list.pop(0)
    
    texts_list = texts_list[char_count:]

print("".join(final_string))