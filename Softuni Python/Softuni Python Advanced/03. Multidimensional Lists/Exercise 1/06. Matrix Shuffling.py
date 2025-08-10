def print_matrix(matrix):
    for r in matrix:
        print(*r)

def swap(matrix, indexes):
    cell_one = matrix[indexes[0]][indexes[1]]
    cell_two = matrix[indexes[2]][indexes[3]]
    
    matrix[indexes[0]][indexes[1]] = cell_two
    matrix[indexes[2]][indexes[3]] = cell_one

    print_matrix(matrix)


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command = input()

    if command == "END":
        break

    invalid_input = False

    if not command.startswith("swap "):
        invalid_input = True

    if not invalid_input:
        command = command[5:]
        indexes = command.split()
        if len(indexes) != 4: invalid_input = True
        elif not all([x.isdigit() for x in indexes]):
            invalid_input = True

        elif int(indexes[0]) not in range(rows) or int(indexes[2]) not in range(rows) \
            or int(indexes[1]) not in range(cols) or int(indexes[3]) not in range(cols):
            invalid_input = True
    
    if invalid_input:
        print("Invalid input!")
        continue

    swap(matrix, [int(x) for x in indexes])