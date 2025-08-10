rows, cols = map(int, input().split())

matrix = [input().split() for _ in range(rows)]

number_squares = 0

if rows >= 2 and cols >= 2:
    for ridx in range(rows - 1):
        for cidx in range(cols - 1):
            if matrix[ridx][cidx] == matrix[ridx][cidx + 1] == matrix[ridx + 1][cidx] == matrix[ridx + 1][cidx + 1]:
                number_squares += 1

print(number_squares)
    



