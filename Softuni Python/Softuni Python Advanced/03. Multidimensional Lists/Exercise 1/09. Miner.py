from collections import deque

field_size = int(input())

commands = list(reversed(input().split()))

field = [] #[['*'] * field_size] * field_size

miner_ridx, miner_cidx = 0, 0

collected_coal = 0
step_on_mine = False

for _ in range(field_size):
    field.append(input().split())


for ridx in range(field_size):
    for cidx in range(field_size):
        if field[ridx][cidx] == "s":
            miner_ridx = ridx
            miner_cidx = cidx
            break

while commands and not step_on_mine:
    command = commands.pop()

    move_pos = [0, 0]

    match command:
        case "up":
            move_pos = [-1, 0]
        case "down":
            move_pos = [1, 0]
        case "left":
            move_pos = [0, -1]
        case "right":
            move_pos = [0, 1]
    
    miner_new_ridx = miner_ridx + move_pos[0]
    miner_new_cidx = miner_cidx + move_pos[1]

    if miner_new_ridx not in range(field_size) or miner_new_cidx not in range(field_size):
        continue

    match field[miner_new_ridx][miner_new_cidx]:
        case "c":
            collected_coal += 1
        case "e":
            step_on_mine = True
        case _:
            pass
    
    field[miner_ridx][miner_cidx] = "*"
    miner_ridx, miner_cidx = miner_new_ridx, miner_new_cidx
    field[miner_ridx][miner_cidx] = "s"

coal_left = len([c for r in field for c in r if c == "c"])

if step_on_mine:
    print(f"Game over! ({miner_ridx}, {miner_cidx})")

elif coal_left:
    print(f"{coal_left} pieces of coal left. ({miner_ridx}, {miner_cidx})")

else:
    print(f"You collected all coal! ({miner_ridx}, {miner_cidx})")