def get_initital_position() -> tuple:
    pos_data = input().split(", ")
    return int(pos_data[0][1:]), int(pos_data[1][:-1])

MATRIX_SIZE = 6
END_COMMAND = "Stop"

mtrx = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for _ in range(MATRIX_SIZE):
    row = input().split()
    '''
    for idx in range(len(row)):
        if row[idx].isdigit():
            row[idx] = int(row[idx])
    '''
    mtrx += [row]

current_position = get_initital_position()

while True:
    command, *args = input().split(", ")

    if command == END_COMMAND:
        break

    current_direction = directions[args[0]]
    current_position_ridx, current_position_cidx = current_position[0] + current_direction[0], current_position[1] + current_direction[1]

    if command == "Create":
        if mtrx[current_position_ridx][current_position_cidx] == ".":
            mtrx[current_position_ridx][current_position_cidx] = args[1]
    
    elif command == "Update":

        if mtrx[current_position_ridx][current_position_cidx] != ".":
            mtrx[current_position_ridx][current_position_cidx] = args[1]
    
    elif command == "Delete":

        mtrx[current_position_ridx][current_position_cidx] = "."
    
    elif command == "Read":
        if mtrx[current_position_ridx][current_position_cidx] != ".":
            print(mtrx[current_position_ridx][current_position_cidx])
    
    current_position = [current_position_ridx, current_position_cidx]

for row in mtrx:
    print(*row)  