cupboard_rows, cupboard_cols = map(int, input().split(","))

cupboard = []
cheeses = []
traps = []
walls = []
mouse_pos = [-1, -1]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

END_COMMAND = 'danger'

MOUSE_CHAR = 'M'
CHEESE_CHAR = 'C'
EMPTY_CHAR = '*'
WALL_CHAR = '@'
TRAP_CHAR = 'T'

for ridx in range(cupboard_rows):
    row = list(input())
    for cidx in range(cupboard_cols):
        pos = [ridx, cidx]
        if row[cidx] == MOUSE_CHAR:
            mouse_pos = pos
        elif row[cidx] == CHEESE_CHAR:
            cheeses += [pos]
        elif row[cidx] == WALL_CHAR:
            walls += [pos]
        elif row[cidx] == TRAP_CHAR:
            traps += [pos]
    cupboard.append(row)

has_trapped, has_stepped, has_exit, has_finished = False, False, False, False

while not has_trapped and not has_stepped and not has_exit and not has_finished:
    try:
        direction = directions[input().lower()]
    except KeyError:
        has_exit = True
        break

    new_mouse_ridx, new_mouse_cidx = mouse_pos
    new_mouse_ridx += direction[0]
    new_mouse_cidx += direction[1]
    new_mouse_pos = [new_mouse_ridx, new_mouse_cidx]

    if not 0 <= new_mouse_ridx < cupboard_rows or not 0 <= new_mouse_cidx < cupboard_cols:
        has_stepped = True
        break

    if new_mouse_pos in traps:
        has_trapped = True

    elif new_mouse_pos in cheeses:
        cheeses.remove(new_mouse_pos)
        if not cheeses:
            has_finished = True


    elif new_mouse_pos in walls:
        continue

    cupboard[mouse_pos[0]][mouse_pos[1]] = EMPTY_CHAR
    cupboard[new_mouse_ridx][new_mouse_cidx] = MOUSE_CHAR
    mouse_pos = [new_mouse_ridx, new_mouse_cidx]

if has_stepped:
    print("No more cheese for tonight!")
elif has_trapped:
    print("Mouse is trapped!")
elif has_exit:
    print("Mouse will come back later!")
elif has_finished:
    print("Happy mouse! All the cheese is eaten, good night!")

for row in cupboard:
    print(*row, sep="")