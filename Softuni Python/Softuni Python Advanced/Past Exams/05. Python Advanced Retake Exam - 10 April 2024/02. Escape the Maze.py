field_size = int(input())

maze = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

PLAYER_CHAR = 'P'
MONSTER_CHAR = 'M'
MAZE_EXIT_CHAR = 'X'
HEALTH_POTION_CHAR = 'H'
CORRIDOR_CHAR = '-'

HEALTH_REDUCE_UNITS = 40
HEALTH_BOOST_UNITS = 15
HEALTH_MAX_UNITS = 100

health = HEALTH_MAX_UNITS
has_escaped_maze = False

player_pos = [-1, -1]
maze_exit_pos = [-1, -1]
monsters = []
health_potions = []

for ridx in range(field_size):
    row = list(input())
    for cidx in range(field_size):
        position = [ridx, cidx]
        if row[cidx] == PLAYER_CHAR:
            player_pos = [ridx, cidx]
        elif row[cidx] == MONSTER_CHAR:
            monsters += [position]
        elif row[cidx] == MAZE_EXIT_CHAR:
            maze_exit_pos = position
        elif row[cidx] == HEALTH_POTION_CHAR:
            health_potions += [position]
    maze.append(row)


while health > 0 and not has_escaped_maze:
    direction = directions[input()]

    new_player_position = [
        player_pos[0] + direction[0],
        player_pos[1] + direction[1]
    ]

    if any(pos not in range(field_size) for pos in new_player_position):
        continue

    if new_player_position in monsters:
        health -= HEALTH_REDUCE_UNITS
        if health > 0:
            monsters.remove(new_player_position)
            maze[new_player_position[0]][new_player_position[1]] = CORRIDOR_CHAR

    elif new_player_position in health_potions:
        health_potions.remove(new_player_position)
        health += HEALTH_BOOST_UNITS
        if health > HEALTH_MAX_UNITS:
            health = HEALTH_MAX_UNITS

    elif new_player_position == maze_exit_pos:
        has_escaped_maze = True

    maze[new_player_position[0]][new_player_position[1]] = PLAYER_CHAR
    maze[player_pos[0]][player_pos[1]] = CORRIDOR_CHAR
    player_pos = new_player_position

if has_escaped_maze:
    print('Player escaped the maze. Danger passed!')
else:
    print('Player is dead. Maze over!')

print(f'Player\'s health: {health if health >= 0 else 0} units')

for row in maze:
    print(''.join(row))