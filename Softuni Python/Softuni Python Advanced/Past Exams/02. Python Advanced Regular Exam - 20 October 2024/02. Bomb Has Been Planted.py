N, M = map(int, input().split(', '))

bomb_pos = [-1, -1]
ct_pos = [-1, -1]
ct_initial_pos = [-1, -1]
terrorists = []
field = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
    "defuse": [0, 0]
}

BOMB_EXPLOSION_TIME = 16
BOMB_DEFUSE_TIME = 4

time_left = BOMB_EXPLOSION_TIME+1
has_won, has_lost, has_killed = False, False, False

for ridx in range(N):
    row = input()
    for cidx in range(M):
        if row[cidx] == 'B':
            bomb_pos = [ridx, cidx]
        elif row[cidx] == 'C':
            ct_pos = [ridx, cidx]
            ct_initial_pos = [ridx, cidx]
        elif row[cidx] == 'T':
            terrorists += [[ridx, cidx]]
    field.append(list(row))

while time_left > 0 and not has_won and not has_lost and not has_killed:
    time_left -= 1
    if time_left == 0:
        has_lost = True
        field[ct_pos[0]][ct_pos[1]] = '*'
        continue
    command = input()
    if command == 'defuse':
        if ct_pos != bomb_pos:
            time_left -= 1
        else:
            time_left -= BOMB_DEFUSE_TIME
            if time_left >= 0:
                has_won = True
                field[ct_pos[0]][ct_pos[1]] = 'D'
            else:
                has_lost = True
                field[ct_pos[0]][ct_pos[1]] = 'X'
        continue
    x, y = directions[command]
    new_ct_pos = [ct_pos[0] + x, ct_pos[1] + y]
    if field[ct_pos[0]][ct_pos[1]] not in 'BDX':
        field[ct_pos[0]][ct_pos[1]] = '*'

    if new_ct_pos[0] not in range(N) or new_ct_pos[1] not in range(M):
        continue

    elif new_ct_pos in terrorists:
        has_lost = True
        has_killed = True
        terrorists.remove(new_ct_pos)
        field[new_ct_pos[0]][new_ct_pos[1]] = '*'
        continue

    if field[new_ct_pos[0]][new_ct_pos[1]] not in 'BDX':
        field[new_ct_pos[0]][new_ct_pos[1]] = 'C'
    ct_pos = new_ct_pos

if has_killed:
    print('Terrorists win!')
elif has_lost:
    print('Terrorists win!')
    print('Bomb was not defused successfully!')
    print(f'Time needed: {0 if time_left > 0 else -time_left} second/s.')
elif has_won:
    print('Counter-terrorist wins!')
    print(f'Bomb has been defused: {time_left} second/s remaining.')

field[ct_initial_pos[0]][ct_initial_pos[1]] = 'C'

for row in field:
    print(*row, sep='')






