from re import finditer

pattern = r'\s(([a-z\d]+([\._-]?[a-z\d]+)*)@([a-z]+([\.-]?[a-z]+)*)\.[a-z]+)\b'

matches = finditer(pattern = pattern, string = input())

for m in matches:
    print(m[0])



