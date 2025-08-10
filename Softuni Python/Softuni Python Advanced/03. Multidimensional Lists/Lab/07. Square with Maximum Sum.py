from sys import maxsize

biggest_sum = -maxsize

max_submatrix = []

num_rows, num_cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for _ in range(num_rows)]

for r in range(num_rows - 1):
    for c in range(num_cols - 1):
        submatrix = [[matrix[r][c], matrix[r][c+1]], [matrix[r+1][c], matrix[r+1][c+1]]]
        curr_sum  = sum([x for y in submatrix for x in y if y != []])

        if curr_sum > biggest_sum:
            max_submatrix = submatrix
            biggest_sum = curr_sum

for row in max_submatrix:
    print(*row)

print(biggest_sum)



