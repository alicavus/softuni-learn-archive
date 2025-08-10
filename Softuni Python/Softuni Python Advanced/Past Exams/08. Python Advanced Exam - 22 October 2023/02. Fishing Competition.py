fishing_area_size = int(input())
fishing_area = []

ship_pos_ridx, ship_pos_cidx = -1, -1
whirpolls = []
fishes = {}

SHIP_CHAR = 'S'
WHIRLPOOL_CHAR = 'W'
EMPTY_POS_CHAR = '-'
FISHING_QUOTA = 20
END_COMMAND = 'collect the nets'
has_failed = False
caught_fishes = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for ridx in range(fishing_area_size):
    row = list(input())
    for cidx in range(fishing_area_size):
        if row[cidx] == SHIP_CHAR:
            ship_pos_ridx, ship_pos_cidx = ridx, cidx
        elif row[cidx] == WHIRLPOOL_CHAR:
            whirpolls += [[ridx, cidx]]
        elif row[cidx].isdigit():
            fishes[str([ridx, cidx])] = int(row[cidx])

    fishing_area += [row]


while not has_failed:
    direction = input()

    if direction == END_COMMAND:
        break

    next_ship_ridx = directions[direction][0] + ship_pos_ridx
    next_ship_cidx = directions[direction][1] + ship_pos_cidx

    while next_ship_ridx < 0:
        next_ship_ridx += fishing_area_size
    while next_ship_ridx >= fishing_area_size:
        next_ship_ridx -= fishing_area_size
    while next_ship_cidx < 0:
        next_ship_cidx += fishing_area_size
    while next_ship_cidx >= fishing_area_size:
        next_ship_cidx -= fishing_area_size

    next_ship_pos = [next_ship_ridx, next_ship_cidx]

    if str(next_ship_pos) in fishes:
        caught_fishes += fishes[str(next_ship_pos)]
        del fishes[str(next_ship_pos)]

    elif next_ship_pos in whirpolls:
        has_failed = True
        whirpolls.remove(next_ship_pos)

    fishing_area[ship_pos_ridx][ship_pos_cidx] = EMPTY_POS_CHAR
    ship_pos_ridx, ship_pos_cidx = next_ship_ridx, next_ship_cidx
    fishing_area[ship_pos_ridx][ship_pos_cidx] = SHIP_CHAR

if has_failed:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{ship_pos_ridx},{ship_pos_cidx}]")
else:
    if caught_fishes >= FISHING_QUOTA:
        print(f"Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {FISHING_QUOTA - caught_fishes} tons of fish more.")

    if caught_fishes:
        print(f"Amount of fish caught: {caught_fishes} tons.")

    for row in fishing_area:
        print(''.join(row))



