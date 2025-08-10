words = {}

for word in input().split():
    word = word.lower()
    if word in words:
        words[word] += 1
    else:
        words.update({word:1})


print(" ".join([k for k,v in words.items() if v % 2]))



