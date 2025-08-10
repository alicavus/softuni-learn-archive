text = input()

occurences = {}

for char in text:
    if char not in occurences:
        occurences[char] = 0
    occurences[char] += 1

for char in sorted(occurences.keys()):
    print(f"{char}: {occurences[char]} time/s")