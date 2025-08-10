from re import split
from collections import deque

field_size = int(input())

field = [list(map(int, input().split())) for _ in range(field_size)]

bombs = list(map(int, split('[ ,]', input())))
bombs = deque([bombs[idx], bombs[idx+1]] for idx in range(0, len(bombs)-1, 2))

while bombs:
    bomb_ridx, bomb_cidx = bombs.popleft()

    bomb_value = field[bomb_ridx][bomb_cidx]
    if bomb_value <= 0:
        continue
    field[bomb_ridx][bomb_cidx] -= bomb_value

    for explode_ridx in range(bomb_ridx - 1, bomb_ridx + 2):
        for explode_cidx in range(bomb_cidx - 1, bomb_cidx + 2):
            if explode_ridx not in range(field_size) or explode_cidx not in range(field_size):
                continue
            elif field[explode_ridx][explode_cidx] <= 0:
                continue
            field[explode_ridx][explode_cidx] -= bomb_value

alive_cells = [cell for row in field for cell in row if cell > 0]
print(f"Alive cells: {len(alive_cells)}\nSum: {sum(alive_cells) if alive_cells else 0}")

for row in field:
    print(*row)




