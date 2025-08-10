collected_hazelnuts = 0
goal_hazelnuts = 3

SQUIRREL_CHAR = 's'
HAZELNUTS_CHAR = 'h'
EMPTY_CHAR = '*'
TRAP_CHAR = 't'

squirrel_pos = [-1, -1]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

field_size = int(input())
field = []
commands = input().split(", ")
for ridx in range(field_size):
    row = list(input())
    if SQUIRREL_CHAR in row:
        squirrel_pos = [ridx, row.index(SQUIRREL_CHAR)]
    field += [row]

for command in commands:
    direction = directions[command]
    curr_ridx = squirrel_pos[0] + direction[0]
    curr_cidx = squirrel_pos[1] + direction[1]

    if not 0 <= curr_ridx < field_size or not 0 <= curr_cidx < field_size:
        print("The squirrel is out of the field.")
        break
    elif field[curr_ridx][curr_cidx] == TRAP_CHAR:
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    elif field[curr_ridx][curr_cidx] == HAZELNUTS_CHAR:
        collected_hazelnuts += 1
        field[curr_ridx][curr_cidx] = EMPTY_CHAR
        if collected_hazelnuts == goal_hazelnuts:
            print("Good job! You have collected all hazelnuts!")
            break
    squirrel_pos = [curr_ridx, curr_cidx]

else:
    if collected_hazelnuts != goal_hazelnuts:
        print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")