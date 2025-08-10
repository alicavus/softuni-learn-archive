from re import findall

pattern_name = r'[A-Za-z]'

pattern_score = r'\d'

participants = {name:0 for name in input().split(", ")}

line = input()

while line !=  "end of race":
    name = "".join(findall(pattern=pattern_name, string=line))
    score_digits = [int(x) for x in findall(pattern=pattern_score, string=line)]
    score = sum(score_digits) if score_digits else 0

    if name and name in participants:
        participants[name] += score

    line = input()

participants = dict(sorted(participants.items(), key=lambda item: -item[1]))

first_three = list(participants.keys())[:3]

print(f"""1st place: {first_three[0]}
2nd place: {first_three[1]}
3rd place: {first_three[2]}""")