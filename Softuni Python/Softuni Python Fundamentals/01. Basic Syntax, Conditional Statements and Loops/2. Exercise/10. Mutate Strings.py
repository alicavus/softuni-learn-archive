string_one = input()
string_two = input()

unique_strings = list()

string_len = len(string_one)

for l in range(1, string_len):
    new_string = f"{string_two[:l]}{string_one[l:]}"
    if new_string not in unique_strings and new_string != string_one:
        unique_strings.append(new_string)

if string_two not in unique_strings:
    unique_strings.append(string_two)

print("\n".join(unique_strings))
