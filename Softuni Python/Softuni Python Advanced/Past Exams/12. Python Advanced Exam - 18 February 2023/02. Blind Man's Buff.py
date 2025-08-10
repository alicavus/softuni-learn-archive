playground = []
rows, cols = map(int, input().split())

BLINDMAN_CHAR = 'B'
OBSTACLE_CHAR = 'O'
PLAYERS_CHAR = 'P'
EMPTY_CHAR = '-'
END_COMMAND = 'Finish'
PLAYERS_THRESHOLD = 3

blindman_ridx, blindman_cidx = -1, -1
touched_opponents = 0
blindman_moves = 0
obstacles = []
opponents = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}



for row_idx in range(rows):
    row = input().split()
    for col_idx in range(cols):
        pos = [row_idx, col_idx]
        if row[col_idx] == BLINDMAN_CHAR:
            blindman_ridx, blindman_cidx = pos
        elif row[col_idx] == OBSTACLE_CHAR:
            obstacles.append(pos)
        elif row[col_idx] == PLAYERS_CHAR:
            opponents.append(pos)
    playground.append(row)

while touched_opponents != PLAYERS_THRESHOLD:
    command = input()
    if command == END_COMMAND:
        break

    direction_ridx, direction_cidx = directions[command]
    current_ridx, current_cidx = blindman_ridx + direction_ridx, blindman_cidx + direction_cidx

    if not 0 <= current_ridx < rows or not 0 <= current_cidx < cols:
        continue

    current_pos = [current_ridx, current_cidx]

    if current_pos in obstacles:
        continue

    elif current_pos in opponents:
        opponents.remove(current_pos)
        touched_opponents += 1
        blindman_moves += 1
        playground[current_ridx][current_cidx] = EMPTY_CHAR

    elif playground[current_ridx][current_cidx] == EMPTY_CHAR:
        blindman_moves += 1

    playground[blindman_ridx][blindman_cidx] = EMPTY_CHAR
    blindman_ridx, blindman_cidx = current_ridx, current_cidx
    playground[blindman_ridx][blindman_cidx] = BLINDMAN_CHAR


print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {blindman_moves}")