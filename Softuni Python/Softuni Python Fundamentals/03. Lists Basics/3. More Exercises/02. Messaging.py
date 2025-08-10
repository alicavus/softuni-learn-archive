sequence_of_numbers = input().strip().split(' ')
sentence = input()

encripted_message = ''

for number in sequence_of_numbers:

    idx = sum([int(x) for x in number])

    while idx >= len(sentence):
        idx -= len(sentence)
    
    encripted_message += sentence[idx]
    sentence = sentence[:idx] + sentence[idx+1:]

print(encripted_message)
