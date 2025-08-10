rows, columns = map(int, input().split(", "))

matrix = []
sum_matrix = 0
for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    sum_matrix += sum(row)
    matrix.append(row)

print(sum_matrix, matrix, sep="\n")