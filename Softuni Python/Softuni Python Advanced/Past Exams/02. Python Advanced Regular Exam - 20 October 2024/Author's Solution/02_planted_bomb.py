def execute_command(grid, position, command, time_left):
    x, y = position
    if command == "up" and x > 0:
        x -= 1
    elif command == "down" and x < len(grid) - 1:
        x += 1
    elif command == "left" and y > 0:
        y -= 1
    elif command == "right" and y < len(grid[0]) - 1:
        y += 1
    elif command == "defuse":
        if grid[x][y] == 'B':
            if time_left >= 4:
                grid[x][y] = 'D'
                return position, time_left - 4, "win"
            grid[x][y] = 'X'
            return position, time_left - 4, "defuse_fail"
        return position, time_left - 2, "continue"
    else:
        return position, time_left - 1, "continue"

    time_left -= 1

    if grid[x][y] == 'T':
        grid[x][y] = '*'
        return (x, y), time_left, "terrorist"
    elif grid[x][y] == 'B':
        return (x, y), time_left, "at_bomb"
    return (x, y), time_left, "continue"


# Read dimensions
dimensions = input().split(", ")
n, m = int(dimensions[0]), int(dimensions[1])

# Read and process the grid, find initial position of the counter-terrorist
grid = []
initial_position = None
for i in range(n):
    row = list(input())
    grid.append(row)
    if 'C' in row:
        initial_position = (i, row.index('C'))


position = initial_position
time_left = 16
status = ''
is_won = False

# Read commands
while time_left:
    command = input()
    is_won = False
    position, time_left, status = execute_command(grid, position, command, time_left)
    if status == 'continue':
        continue
    if status == "win":
        print("Counter-terrorist wins!")
        print(f"Bomb has been defused: {time_left} second/s remaining.")
        is_won = True
        break
    if status == "defuse_fail" or status == "terrorist":
        break
    if status == "at_bomb" and time_left <= 0:
        break

if not is_won:
    print("Terrorists win!")
    if not status == "terrorist":
        print("Bomb was not defused successfully!")
        print(f"Time needed: {abs(time_left)} second/s.")


grid[initial_position[0]][initial_position[1]] = 'C'
for row in grid:
    print(''.join(row))