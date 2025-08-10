from re import finditer

pattern = r"([0-9]*)"

text = input()

while text != "":
    matches = finditer(pattern, text)

    for match in matches:
        mg = match.group()

        if mg:
            print(mg, end=" ")

    text=input()