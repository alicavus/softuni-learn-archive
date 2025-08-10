def calculate_snowball(w: int, t: int, q: int) -> int:
    return (w // t) ** q

snowballs = []

max_value = 0

for _ in range(int(input())):
    weight, time, quality = [int(input()) for __ in range(3)]

    d = dict()
    d["weight"] = weight
    d["time"] = time
    d["quality"] = quality
    d["value"] = calculate_snowball(weight, time, quality)

    max_value = max(max_value, d["value"]);

    snowballs.append(d)

for snowball in snowballs:
    if max_value == snowball["value"]:
        print(f'{snowball["weight"]} : {snowball["time"]} = {snowball["value"]} ({snowball["quality"]})')



