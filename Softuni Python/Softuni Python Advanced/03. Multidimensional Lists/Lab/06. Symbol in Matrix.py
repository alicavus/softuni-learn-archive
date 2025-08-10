found = None

matrix = [[x for x in input()] for _ in range(int(input()))]

symbol = input()

for row_idx in range(len(matrix)):
    for col_idx in range(len(matrix[row_idx])):
        if matrix[row_idx][col_idx] == symbol:
            found = f"({row_idx}, {col_idx})"
            break
    if found:
        break

print(f"{symbol} does not occur in the matrix" if found is None else found)