words = {}

for _ in range(int(input())):
    word, synonym = input(), input()
    if word not in words:
        words[word] = []
    
    words[word] += [synonym]

for word in words:
    print(f"{word} - {', '.join(words[word])}")
