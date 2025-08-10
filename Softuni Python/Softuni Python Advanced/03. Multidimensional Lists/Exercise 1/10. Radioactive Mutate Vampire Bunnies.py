rows, cols = [int(x) for x in input().split()]

def reproduce_bunny(field, bunny_ridx, bunny_cidx):
    global rows, cols, cought_on_bunny
    for bunny_mridx in [bunny_ridx - 1, bunny_ridx + 1]:
        if bunny_mridx not in range(rows):
            continue
        match field[bunny_mridx][bunny_cidx]:
            case "P":
                cought_on_bunny = True
            case "B":
                continue
            case _:
                pass
        field[bunny_mridx][bunny_cidx] = "$"

    for bunny_mcidx in [bunny_cidx - 1, bunny_cidx + 1]:
        if bunny_mcidx not in range(cols):
            continue
        match field[bunny_ridx][bunny_mcidx]:
            case "P":
                cought_on_bunny = True
            case "B":
                continue
            case _:
                pass
        
        field[bunny_ridx][bunny_mcidx] = "$"

def reproduce_bunny_done():
    global field, rows, cols
    for r in range(rows):
        for c in range(cols):
            if field[r][c] == "$":
                field[r][c] = "B"
    

field = []

player_ridx = 0
player_cidx = 0

for ridx in range(rows):
    row = input()
    player_pos = row.find("P")

    if player_pos > -1:
        player_ridx = ridx
        player_cidx = player_pos
    
    field.append(list(row))

commands = input()

cought_on_bunny = False
escaped = False

for command in commands:
    player_new_cidx, player_new_ridx = player_cidx, player_ridx
    match command:
        case "L":
            player_new_cidx -= 1
        case "R":
            player_new_cidx += 1
        case "U":
            player_new_ridx -= 1
        case "D":
            player_new_ridx += 1

    field[player_ridx][player_cidx] = "."
    
    if player_new_cidx not in range(cols) or player_new_ridx not in range(rows):
        escaped = True

    if not escaped:
        if field[player_new_ridx][player_new_cidx] == "B":
            cought_on_bunny = True
        else:
            field[player_new_ridx][player_new_cidx] = "P"

        player_ridx = player_new_ridx
        player_cidx = player_new_cidx
    
    for ridx in range(rows):
        for cidx in range(cols):
            if field[ridx][cidx] == "B":
                reproduce_bunny(field, ridx, cidx)
    reproduce_bunny_done()
    if escaped or cought_on_bunny:
        break

for r in field:
    print("".join(r))

print(f"{'won' if escaped else 'dead'}: {player_ridx} {player_cidx}")