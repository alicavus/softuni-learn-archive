battlefield_size = int(input())
battlefield = []

SUBMARINE_CHAR = 'S'
EMPTY_SECTOR_CHAR = '-'
NAVAL_MINE_CHAR = '*'
BATTLE_CRUISER_CHAR = 'C'

WITHSTAND_NAVAL_MINES_COUNT = 2
BATTLE_CRUISER_COUNT = 3

mines = []
cruisers = []
submarine_pos = [-1, -1]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

exploded_mines_count = 0
sunked_cruisers_count = 0

for ridx in range(battlefield_size):
    row = list(input())
    for cidx in range(battlefield_size):
        cur_pos = [ridx, cidx]
        if row[cidx] == SUBMARINE_CHAR:
            submarine_pos = cur_pos
        elif row[cidx] == NAVAL_MINE_CHAR:
            mines += [cur_pos]
        elif row[cidx] == BATTLE_CRUISER_CHAR:
            cruisers += [cur_pos]
    battlefield += [row]

while exploded_mines_count <= WITHSTAND_NAVAL_MINES_COUNT \
    and sunked_cruisers_count < BATTLE_CRUISER_COUNT:

    direction = directions[input()]

    curr_submarine_pos = [submarine_pos[0] + direction[0], submarine_pos[1] + direction[1]]

    if curr_submarine_pos in mines:
        mines.remove(curr_submarine_pos)
        exploded_mines_count += 1

    elif curr_submarine_pos in cruisers:
        cruisers.remove(curr_submarine_pos)
        sunked_cruisers_count += 1

    battlefield[submarine_pos[0]][submarine_pos[1]] = EMPTY_SECTOR_CHAR
    submarine_pos = curr_submarine_pos
    battlefield[submarine_pos[0]][submarine_pos[1]] = SUBMARINE_CHAR

if exploded_mines_count > WITHSTAND_NAVAL_MINES_COUNT:
    print(f"Mission failed, U-9 disappeared! Last known coordinates {list(submarine_pos)}!")

if sunked_cruisers_count == BATTLE_CRUISER_COUNT:
    print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

for row in battlefield:
    print(*row, sep='')