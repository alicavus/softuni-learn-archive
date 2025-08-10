def shot_target(value: int) -> None:
    global cur_value
    
    if value == -1:
        return -1
    if value > cur_value:
        return value - cur_value
    return cur_value + value

shot_targets = list(map(int, input().split()))
shots_count = 0

while True:
    command = input()

    if command == "End":
        print(f"Shot targets: {shots_count} -> {' '.join(map(str, shot_targets))}")
        break

    idx_to_shot = int(command)

    if idx_to_shot not in range(len(shot_targets)):
        continue

    cur_value = shot_targets[idx_to_shot]
    
    shot_targets[idx_to_shot] = -1

    if cur_value == -1:
        continue

    shots_count += 1

    shot_targets = list(map(shot_target, shot_targets))


