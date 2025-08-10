FIELD_SIZE = 5

field = []
targets = []
hits = []

assassin = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for ridx in range(FIELD_SIZE):
    row = input().split()
    if "A" in row:
        assassin = [ridx, row.index("A")]
    if "x" in row:
        for idx in range(len(row)):
            if row[idx] == "x":
                targets.append([ridx, idx])
    field.append(row)

for _ in range(int(input())):
    commands = input().split()
    command, direction = commands[:2]

    if command == "move":
        steps_count = int(commands[2])
        path = [[step * directions[direction][0] + assassin[0], step * directions[direction][1] + assassin[1]] for step in range(1, steps_count+1, 1)]
        if steps_count * directions[direction][0] + assassin[0] not in range(FIELD_SIZE) \
            or steps_count * directions[direction][1] + assassin[1] not in range(FIELD_SIZE):
            continue
        elif any([p in targets for p in path]):
            continue
        if field[path[-1][0]][path[-1][1]] == ".":
            assassin = path[-1]

    elif command == "shoot":
        current_target = assassin.copy()
        while True:
            current_target[0] += directions[direction][0]
            current_target[1] += directions[direction][1]
            
            if current_target[0] not in range(FIELD_SIZE) or current_target[1] not in range(FIELD_SIZE):
                break
            elif current_target in targets:
                hits.append(current_target.copy())
                targets.remove(current_target)
                break

        if len(targets) == 0:
            break

targets_left = len(targets)
hit_targets = len(hits)

print(f"Training not completed! {targets_left} targets left." if targets_left else f"Training completed! All {hit_targets} targets hit.")

for tg in hits:
    print(tg)