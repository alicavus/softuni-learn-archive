field_size = int(input())

field = []

BEE_CHAR = 'B'
HIVE_CHAR = 'H'
EMPTY_CHAR = "-"

bee_position = [-1, -1]
hive_position = [-1, -1]
nectars = {}
collected_nectar = 0

has_refilled = False

bee_energy = 15
nectar_threshold = 30

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for ridx in range(field_size):
    row = list(input())
    for cidx in range(field_size):
        curr_position = [ridx, cidx]
        if row[cidx] == BEE_CHAR:
            bee_position = curr_position
        elif row[cidx] == HIVE_CHAR:
            hive_position = curr_position
        elif row[cidx].isdigit():
            nectars[str(curr_position)] = int(row[cidx])
    field.append(row)

while bee_energy >= 0 and bee_position != hive_position:
    if bee_energy == 0:
        if collected_nectar < nectar_threshold or has_refilled:
            break

        refill_amount = collected_nectar - nectar_threshold

        if refill_amount > 0:
            bee_energy += refill_amount
            collected_nectar = nectar_threshold
            has_refilled = True

    direction = directions[input()]
    new_bee_position = [
        bee_position[0] + direction[0],
        bee_position[1] + direction[1]
    ]

    if new_bee_position[0] not in range(field_size):
        new_bee_position[0] = 0 if new_bee_position[0] >= field_size else field_size - 1

    if new_bee_position[1] not in range(field_size):
        new_bee_position[1] = 0 if new_bee_position[1] >= field_size else field_size - 1

    if str(new_bee_position) in nectars:
        collected_nectar += nectars[str(new_bee_position)]
        del nectars[str(new_bee_position)]
        field[new_bee_position[0]][new_bee_position[1]] = EMPTY_CHAR

    field[new_bee_position[0]][new_bee_position[1]] = BEE_CHAR
    field[bee_position[0]][bee_position[1]] = EMPTY_CHAR
    bee_position = new_bee_position
    bee_energy -= 1


if bee_position == hive_position:
    if collected_nectar >= nectar_threshold:
        print(f'Great job, Beesy! The hive is full. Energy left: {bee_energy}')
    else:
        print(f'Beesy did not manage to collect enough nectar.')
else:
    print(f'This is the end! Beesy ran out of energy.')

for row in field:
    print(''.join(row))