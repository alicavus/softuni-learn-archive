sequence_one, sequence_two = input().split(", "), input().split(", ")

substrings_of_seq_two = []

for word_one in sequence_one:
    for word_two in sequence_two:
        if word_one in word_two:
            substrings_of_seq_two += [word_one]
            break

print(substrings_of_seq_two)