def move_bee(matrix, direction, bee_position, energy, nectar_collected, restored_energy):
    n = len(matrix)
    x, y = bee_position

    if direction == "up":
        x = (x - 1) % n
    elif direction == "down":
        x = (x + 1) % n
    elif direction == "left":
        y = (y - 1) % n
    elif direction == "right":
        y = (y + 1) % n

    energy -= 1

    if matrix[x][y].isdigit():
        nectar_collected += int(matrix[x][y])
        matrix[x][y] = '-'

    if energy <= 0 and not restored_energy and nectar_collected >= 30:
        restored_energy = True
        energy += nectar_collected - 30
        nectar_collected = 30

    return (x, y), energy, nectar_collected, restored_energy


# Read input
n = int(input().strip())
matrix = []
bee_position = None

# Fill the matrix and find the bee's initial position
for i in range(n):
    row = list(input().strip())
    if 'B' in row:
        bee_position = (i, row.index('B'))
    matrix.append(row)

energy = 15
nectar_collected = 0
restored_energy = False

while True:
    command = input().strip()
    bee_position, energy, nectar_collected, restored_energy = move_bee(matrix, command, bee_position, energy,
                                                                       nectar_collected, restored_energy)
    x, y = bee_position

    if matrix[x][y] == 'H':
        if nectar_collected >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    if energy <= 0:
        print("This is the end! Beesy ran out of energy.")
        break

# Update the bee's final position
final_matrix = [['-' if matrix[i][j] == 'B' else matrix[i][j] for j in range(n)] for i in range(n)]
final_matrix[bee_position[0]][bee_position[1]] = 'B'

for row in final_matrix:
    print(''.join(row))