rows, cols = map(int, input().split(", "))

matrix = []

for r_idx in range(rows):
    matrix.append([int(x) for x in input().split()])

cols_sums = []

for c_idx in range(cols):
    curr_sum = 0
    for r_idx in range(rows):
        curr_sum += matrix[r_idx][c_idx]
    cols_sums.append(curr_sum)

print(*cols_sums, sep="\n")