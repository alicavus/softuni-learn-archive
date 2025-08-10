field_size = int(input())

field = []

spaceship = [-1, -1]
goal_planet = [-1, -1]
meteorites = []
stations = []

has_won, has_failed = False, False
resources = 100

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for row_idx in range(field_size):
    row = input().split()

    for idx in range(len(row)):
        match row[idx]:
            case "M":
                meteorites.append([
                    row_idx,
                    idx
                ])
            case "R":
                stations.append([
                    row_idx,
                    idx
                ])
            case "P":
                goal_planet = [
                    row_idx,
                    idx
                ]
            case "S":
                spaceship = [
                    row_idx,
                    idx
                ]
    field.append(row)


while not has_failed and not has_won:

    resources -= 5

    if resources < 0:
        has_failed = True
        break

    direction = directions[input()]

    new_position = [
        spaceship[0] + direction[0],
        spaceship[1] + direction[1]
    ]

    if any([pos not in range(field_size) for pos in new_position]):
        has_failed = True
        break
    
    match field[new_position[0]][new_position[1]]:
        case ".":
            field[new_position[0]][new_position[1]] = "S"
        case "P":
            has_won = True
        case "M":
            resources -= 5
            field[new_position[0]][new_position[1]] = "S"
            if resources < 0:
                has_failed = True
                break
        case "R":
            resources += 10
            if resources > 100:
                resources = 100
    if field[spaceship[0]][spaceship[1]] not in "RP":
        field[spaceship[0]][spaceship[1]] = "."
    spaceship = new_position

if has_failed:
    if resources < 0:
        print("Mission failed! The spaceship was stranded in space.")
    else:
        print("Mission failed! The spaceship was lost in space.")

elif has_won:
    print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")

for row in field:
    print(*row)