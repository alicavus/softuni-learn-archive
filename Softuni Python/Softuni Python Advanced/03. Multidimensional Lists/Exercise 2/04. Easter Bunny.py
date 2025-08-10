field_size = int(input())
field = []
bunny_ridx, bunny_cidx = 0, 0
traps = []

eggs = {
    "right": {"indices": [], "count": 0},
    "left": {"indices": [], "count": 0},
    "up": {"indices": [], "count": 0},
    "down": {"indices": [], "count": 0}
}

directions = {
    "right": [0, 1],
    "left": [0, -1],
    "up": [-1, 0],
    "down": [1, 0]
}

for ridx in range(field_size):
    row = input().split()

    if "B" in row:
        bunny_ridx = ridx
        bunny_cidx = row.index("B")
    
    cur_cix = 0

    while "X" in row[cur_cix:]:
        idx = row.index("X", cur_cix)
        traps.append([ridx, idx])
        cur_cix = idx + 1
    
    field.append(row)

for direction in directions:
    cur_bunny_ridx, cur_bunny_cidx = bunny_ridx, bunny_cidx
    while True:
        cur_bunny_ridx, cur_bunny_cidx = cur_bunny_ridx + directions[direction][0], cur_bunny_cidx + directions[direction][1]
        if cur_bunny_ridx not in range(field_size) or cur_bunny_cidx not in range(field_size) \
            or [cur_bunny_ridx, cur_bunny_cidx] in traps:
            break
        eggs[direction]["indices"].append([cur_bunny_ridx, cur_bunny_cidx])
        eggs[direction]["count"] += int(field[cur_bunny_ridx][cur_bunny_cidx])


direction = sorted(eggs, key=lambda x: eggs[x]["count"], reverse=True)[0]

print(direction, *eggs[direction]["indices"], eggs[direction]["count"], sep="\n")