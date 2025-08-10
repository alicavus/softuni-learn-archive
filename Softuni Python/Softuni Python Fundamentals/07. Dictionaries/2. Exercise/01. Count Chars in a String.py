
my_dict = {}

for c in input():
    if c == " ":
        continue
    if c not in my_dict:
        my_dict[c] = 0
    my_dict[c] += 1

for c in my_dict:
    print(f'{c} -> {my_dict[c]}')