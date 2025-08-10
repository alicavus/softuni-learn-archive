field_size = int(input())
wonderland = []

alice = [0, 0]

tea = {
    "count": 0,
    "target": 10
}

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

rabbitholes = []

for ridx in range(field_size):
    row = input().split()
    if "A" in row:
        alice = [ridx, row.index("A")]
        row[alice[1]] = '*'
    if "R" in row:
        rabbitholes += [ridx, row.index("R")]
    wonderland.append(row)

while True:
    direction = input()
    alice = [alice[0] + directions[direction][0], alice[1] + directions[direction][1]]

    if any([x not in range(field_size) for x in alice]):
        break
    cur_symbol = wonderland[alice[0]][alice[1]]

    if cur_symbol == "R":
        wonderland[alice[0]][alice[1]] = "*"
        break

    elif cur_symbol.isdigit():
        tea["count"] += int(cur_symbol)
        
    wonderland[alice[0]][alice[1]] = "*"
    
    if tea["count"] >= tea["target"]:
        break

print("She did it! She went to the party." if tea["count"] >= tea["target"] else "Alice didn't make it to the tea party.")

for row in wonderland:
    print(*row)