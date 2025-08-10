presents = int(input())
size = int(input())

santa = []

naughty_kids = []
nice_kids = []
cookies = []

presents_nice_kids = 0

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

field = []

for ridx in range(size):
    row = input().split()
    for idx in range(len(row)):
        match row[idx]:
            case "S":
                santa = [ridx, idx]
            case "C":
                cookies.append([ridx, idx])
            case "V":
                nice_kids.append([ridx, idx])
            case "X":
                naughty_kids.append([ridx, idx])
    field.append(row)

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    
    santa_ridx, santa_cidx = santa
    santa_ridx += directions[command][0]
    santa_cidx += directions[command][1]

    if santa_ridx not in range(size) or santa_cidx not in range(size):
        continue

    cell = [santa_ridx, santa_cidx]

    if cell in nice_kids:
        presents_nice_kids += 1
        presents -= 1
        nice_kids.remove(cell)
    
    elif cell in cookies:
        for d in directions.keys():
            if presents <= 0:
                break
            neighbor = cell.copy()
            neighbor[0] += directions[d][0]
            neighbor[1] += directions[d][1]
            if any([x not in range(size) for x in neighbor]):
                continue
            if neighbor in nice_kids:
                presents_nice_kids += 1
                nice_kids.remove(neighbor)
            elif neighbor in naughty_kids:
                naughty_kids.remove(neighbor)

            presents -= 1
            field[neighbor[0]][neighbor[1]] = "-"
        cookies.remove(cell)
    field[santa[0]][santa[1]] = "-"
    santa = cell
    field[santa[0]][santa[1]] = "S"


if nice_kids and presents <= 0:
    print("Santa ran out of presents!")

for row in field:
    print(*row)


print(f"Good job, Santa! {presents_nice_kids} happy nice kid/s." if not nice_kids else f"No presents for {len(nice_kids)} nice kid/s.")