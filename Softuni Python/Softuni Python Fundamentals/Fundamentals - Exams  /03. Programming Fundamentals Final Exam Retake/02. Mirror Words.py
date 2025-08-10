import re

text = input()

result = re.findall(r'#([a-zA-Z]{3,})##([a-zA-Z]{3,})#|@([a-zA-Z]{3,})@@([a-zA-Z]{3,})@', text)

pairs = []

if result == []:
    print("No word pairs found!")
else:
    print(f"{len(result)} word pairs found!")
    for words in result:
        words = list(filter(lambda x : len(x), words))
        if words[0] == words[1][::-1]:
            pairs.append(f"{words[0]} <=> {words[1]}")

if pairs == []:
    print("No mirror words!")
else:
    print(f"The mirror words are:")
    print(", ".join(pairs))

