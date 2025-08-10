from re import findall

pattern = r"\b_([A-Za-z0-9]*)\b"

text = input()

print(",".join(findall(pattern=pattern, string=text)))