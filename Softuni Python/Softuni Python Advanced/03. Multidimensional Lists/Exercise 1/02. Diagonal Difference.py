rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary_diagoanal = sum([matrix[x][x] for x in range(rows)])
secondary_diagoanal = sum([matrix[x][rows - x - 1] for x in range(rows)])

print(abs(primary_diagoanal - secondary_diagoanal))