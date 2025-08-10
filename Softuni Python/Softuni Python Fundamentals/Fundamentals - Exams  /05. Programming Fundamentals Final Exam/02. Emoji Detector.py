from re import findall
from functools import reduce

emoji_pattern = r'::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*'

sentence = input()

cool_threshold_digits = [int(x) for x in sentence if x.isdigit()]
cool_threshold = reduce(lambda x, y: x*y, cool_threshold_digits)

valid_emojies = findall(emoji_pattern, sentence)

cool_emojies = []

for emoji in valid_emojies:
    emoji_coolnes = sum([ord(x) for x in emoji[2:-2]])
    if emoji_coolnes >= cool_threshold:
        cool_emojies += [emoji]

print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojies)} emojis found in the text. The cool ones are:")
print("\n".join(cool_emojies))