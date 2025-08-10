n = int(input())
health = 100
maze = []
prow, pcol = None, None

movements = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for r in range(n):
    maze.append([ch for ch in input()])
    for c in range(n):
        if maze[r][c] == "P":
            prow, pcol = r, c

while True:
    move = input()

    if not (0 <= prow + movements[move][0] < n and 0 <= pcol + movements[move][1] < n):
        continue

    maze[prow][pcol] = "-"
    prow += movements[move][0]
    pcol += movements[move][1]

    if maze[prow][pcol] == "X":
        print("Player escaped the maze. Danger passed!")
        maze[prow][pcol] = "P"
        break

    elif maze[prow][pcol] == "H":
        health = min(100, health + 15)

    elif maze[prow][pcol] == "M":
        health -= 40
        if health <= 0:
            health = 0
            print("Player is dead. Maze over!")
            maze[prow][pcol] = "P"
            break

    maze[prow][pcol] = "P"

print(f"Player's health: {health} units")
for row in maze:
    print(''.join(row))