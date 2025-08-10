airspace_size = int(input())

airspace = []

jetfighter_pos = [-1, -1]
enemies = []
repair_posts = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

JETFIGHTER_CHAR = 'J'
ENEMY_CHAR = 'E'
REPAIR_POINT_CHAR = 'R'
EMPTY_CHAR = '-'
ARMOUR_DAMAGE_POINTS = 100
ARMOUR_INITIAL_POINTS = 300

armour = ARMOUR_INITIAL_POINTS

for rowidx in range(airspace_size):
    row = list(input())
    for colidx in range(airspace_size):
        pos = [rowidx, colidx]
        if row[colidx] == JETFIGHTER_CHAR:
            jetfighter_pos = pos

        elif row[colidx] == REPAIR_POINT_CHAR:
            repair_posts += [pos]

        elif row[colidx] == ENEMY_CHAR:
            enemies += [pos]

    airspace += [row]

while enemies and armour > 0:
    dir_ridx, dir_cidx = directions[input()]

    new_pos_ridx = dir_ridx + jetfighter_pos[0]
    new_pos_cidx = dir_cidx + jetfighter_pos[1]

    new_pos = [new_pos_ridx, new_pos_cidx]

    if new_pos in repair_posts:
        repair_posts.remove(new_pos)
        armour = ARMOUR_INITIAL_POINTS

    elif new_pos in enemies:
        enemies.remove(new_pos)

        if enemies:
            armour -= ARMOUR_DAMAGE_POINTS

    airspace[jetfighter_pos[0]][jetfighter_pos[1]] = EMPTY_CHAR
    jetfighter_pos = new_pos
    airspace[new_pos_ridx][new_pos_cidx] = JETFIGHTER_CHAR


if not enemies:
    print('Mission accomplished, you neutralized the aerial threat!')

elif armour <= 0:
    print(f'Mission failed, your jetfighter was shot down! Last coordinates {jetfighter_pos}!')

for row in airspace:
    print("".join(row))







