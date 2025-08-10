matrix_size = int(input())
racing_number = input()

car_pos = [0, 0]
tunnel_pos = []
finish_pos = [-1, -1]

TUNNEL_CHAR = 'T'
FINISH_LINE_CHAR = 'F'
EMPTY_ROUTE_CHAR = '.'
CAR_CHAR = 'C'
END_COMMAND = 'End'

KM_PER_NORMAL_MOVE = 10
KM_PER_TUNNEL_MOVE = 30

has_finished = False
has_ended = False

race_route = []

distance = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for ridx in range(matrix_size):
    row = input().split()
    for cidx in range(matrix_size):
        pos = [ridx, cidx]
        if row[cidx] == TUNNEL_CHAR:
            tunnel_pos.append(pos)
        elif row[cidx] == FINISH_LINE_CHAR:
            finish_pos = pos

    race_route.append(row)


race_route[0][0] = CAR_CHAR

while not has_finished and not has_ended:
    curr_command = input()

    if curr_command == END_COMMAND:
        has_ended = True
        break

    curr_move = directions[curr_command]
    curr_pos = [car_pos[0] + curr_move[0], car_pos[1] + curr_move[1]]

    distance += KM_PER_NORMAL_MOVE

    if curr_pos == finish_pos:
        has_finished = True

    elif curr_pos in tunnel_pos:
        distance += KM_PER_TUNNEL_MOVE
        distance -= KM_PER_NORMAL_MOVE

        tunnel_pos.remove(curr_pos)
        race_route[curr_pos[0]][curr_pos[1]] = EMPTY_ROUTE_CHAR
        curr_pos = tunnel_pos.pop()

    race_route[car_pos[0]][car_pos[1]] = EMPTY_ROUTE_CHAR
    car_pos = curr_pos
    race_route[car_pos[0]][car_pos[1]] = CAR_CHAR

if has_finished:
    print(f"Racing car {racing_number} finished the stage!")

elif has_ended:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {distance} km.")

for row in race_route:
    print(''.join(row))