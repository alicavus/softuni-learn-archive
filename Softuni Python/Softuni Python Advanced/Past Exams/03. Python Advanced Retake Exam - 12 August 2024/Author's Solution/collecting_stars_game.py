def move_player(field, position, direction):
    n = len(field)
    row, col = position
    if direction == 'up':
        row -= 1
    elif direction == 'down':
        row += 1
    elif direction == 'left':
        col -= 1
    elif direction == 'right':
        col += 1

    if (row < 0 or row >= n or col < 0 or col >= n) and field[0][0] == '*':
        field[0][0] = '.'
        return (0, 0), 1  # Teleport to (0, 0), gain one star
    if row < 0 or row >= n or col < 0 or col >= n:
        return (0, 0), 0  # Teleport to (0, 0), no star change
    if field[row][col] == '#':
        return position, -1  # Hit an obstacle, lose one star, no change in position
    if field[row][col] == '*':
        field[row][col] = '.'
        return (row, col), 1  # Collect a star, gain one star
    return (row, col), 0  # Move to an empty cell


# Initial state
stars = 2
player_pos = (None, None)
field = []

n = int(input())

for i in range(n):
    field.append(input().split(' '))
    for j in range(n):
        if field[i][j] == 'P':
            player_pos = (i, j)
            field[i][j] = '.'


# Reading commands
while True:
    command = input()
    player_pos, star_change = move_player(field, player_pos, command)
    stars += star_change
    if stars >= 10:
        print("You won! You have collected 10 stars.")
        break
    if stars <= 0:
        print("Game over! You are out of any stars.")
        break

# Final position and final field state
final_row, final_col = player_pos
field[final_row][final_col] = 'P'

print(f"Your final position is [{final_row}, {final_col}]")
for row in field:
    print(' '.join(row))






