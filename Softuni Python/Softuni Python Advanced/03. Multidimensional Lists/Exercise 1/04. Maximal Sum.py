from sys import maxsize

maxsum = -maxsize
maxmatrix = []

rows, cols = map(int, input().split())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for ridx in range(rows - 2):
    for cidx in range(cols - 2):
        curmatrix = [
            [matrix[ridx][cidx], matrix[ridx][cidx+1], matrix[ridx][cidx+2]],
            [matrix[ridx+1][cidx], matrix[ridx+1][cidx+1], matrix[ridx+1][cidx+2]],
            [matrix[ridx+2][cidx], matrix[ridx+2][cidx+1], matrix[ridx+2][cidx+2]]
        ]
        cur_sum = sum([x for r in curmatrix for x in r])

        if cur_sum > maxsum:
            maxmatrix = curmatrix
            maxsum = cur_sum

print(f"Sum = {maxsum}")
for r in maxmatrix:
    print(*r)
