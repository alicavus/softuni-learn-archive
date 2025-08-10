rows = int(input())

matrix = [list(map(int, input().split())) for _ in range(rows)]

while True:
    commands = input().split()

    if commands[0] == "END":
        break

    ridx, cidx, value = map(int, commands[1:])

    if ridx not in range(rows) or cidx not in range(rows):
        print("Invalid coordinates")
        continue

    matrix[ridx][cidx] += value if commands[0] == "Add" else -value


for r in matrix:
    print(*r)