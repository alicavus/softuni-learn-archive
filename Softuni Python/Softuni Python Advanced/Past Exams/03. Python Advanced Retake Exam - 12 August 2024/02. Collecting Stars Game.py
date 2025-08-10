N = int(input())

PLAYER_CHAR = "P"
STAR_CHAR = "*"
OBSTACLE_CHAR = "#"

GOAL_STARS = 10

collected_stars = 2

player_position = [-1, -1]
obstacles = []
stars = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

field = []

for ridx in range(N):
    row = input().split()
    for cidx in range(N):
        pos = [ridx, cidx]

        if row[cidx] == PLAYER_CHAR:
            player_position = pos

        elif row[cidx] == STAR_CHAR:
            stars.append(pos)

        elif row[cidx] == OBSTACLE_CHAR:
            obstacles.append(pos)

    field.append(row)


while 0 < collected_stars < GOAL_STARS:
    direction = input()

    new_player_position = [
        player_position[0] + directions[direction][0],
        player_position[1] + directions[direction][1]
    ]

    if any(pos not in range(N) for pos in new_player_position):
        if new_player_position not in obstacles:
            new_player_position = [0, 0]
        else:
            collected_stars -= 1

    if new_player_position in obstacles:
        collected_stars -= 1

    else:
        if new_player_position in stars:
            stars.remove(new_player_position)
            collected_stars += 1

        field[new_player_position[0]][new_player_position[1]] = PLAYER_CHAR
        field[player_position[0]][player_position[1]] = "."

        player_position = new_player_position


if collected_stars == GOAL_STARS:
    print(f"You won! You have collected {collected_stars} stars.")
else:
    print("Game over! You are out of any stars.")

print("Your final position is", player_position)

for row in field:
    print(*row)

