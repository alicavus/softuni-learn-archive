sea_map = []
map_size = int(input())

SHIP_CHAR = 'S'
TREASURE_CHEST_CHAR = '*'
MONSTER_CHAR = 'M'
CHARM_CHAR = 'C'
EMPTY_CHAR = '.'

STARTING_DURABILITY = 100
MAXIMUM_DURABILITY = STARTING_DURABILITY
CHANGE_DURABILITY = 25

STOP_COMMAND = 'stop'

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

ship_pos = [-1, -1]
treasures = []
monsters = []
charms = []

durability = STARTING_DURABILITY
has_retreat = False
has_refilled = False

for ridx in range(map_size):
    row = list(input())
    for cidx in range(map_size):
        pos = [ridx, cidx]
        
        if row[cidx] == SHIP_CHAR:
            ship_pos = pos
        
        elif row[cidx] == CHARM_CHAR:
            charms += [pos]
        
        elif row[cidx] == MONSTER_CHAR:
            monsters += [pos]
        
        elif row[cidx] == TREASURE_CHEST_CHAR:
            treasures += [pos]
    sea_map += [row]

while treasures and durability > 0 and not has_retreat:
    command = input()

    if command == STOP_COMMAND:
        has_retreat = True
        break

    direction = directions[command]

    curr_ship_pos = [ship_pos[0] + direction[0], ship_pos[1] + direction[1]]

    if not all(0 <= pos < map_size for pos in curr_ship_pos):
        curr_ship_pos = [
            curr_ship_pos[0] % map_size,
            curr_ship_pos[1] % map_size
        ]
    
    if curr_ship_pos in charms:
        charms.remove(curr_ship_pos)
        if not has_refilled:
            has_refilled = True
            durability += CHANGE_DURABILITY
            if durability > MAXIMUM_DURABILITY:
                durability = MAXIMUM_DURABILITY
    
    elif curr_ship_pos in monsters:
        monsters.remove(curr_ship_pos)
        durability -= CHANGE_DURABILITY
    
    elif curr_ship_pos in treasures:
        treasures.remove(curr_ship_pos)
    
    sea_map[ship_pos[0]][ship_pos[1]] = EMPTY_CHAR
    ship_pos = curr_ship_pos
    sea_map[ship_pos[0]][ship_pos[1]] = SHIP_CHAR

if durability <= 0:
    print(f"Shipwreck! Last known coordinates {tuple(ship_pos)}")

elif not treasures:
    print("Yo-ho-ho! All treasure chests collected!")

elif has_retreat:
    print("Retreat! Some treasures remain unclaimed.")

print(f"Ship Durability: {durability}")

if treasures:
    print(f"Unclaimed chests: {len(treasures)}")

for row in sea_map:
    print(*row, sep='')