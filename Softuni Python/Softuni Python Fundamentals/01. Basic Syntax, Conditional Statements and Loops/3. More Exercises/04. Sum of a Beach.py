def how_many(inp) -> int:
    res = 0
    for word in [x.lower() for x in WORDS]:
        ix = 0
        while inp.find(word, ix) > -1:
            ix = inp.find(word, ix) + 1
            res += 1
    return res


WORDS = ["Sand", "Water", "Fish", "Sun"]

my_input = input().lower()

print(how_many(my_input))