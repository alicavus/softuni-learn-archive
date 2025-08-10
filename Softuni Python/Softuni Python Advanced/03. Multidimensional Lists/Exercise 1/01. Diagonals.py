rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

primary_diagoanal = [matrix[x][x] for x in range(rows)]
secondary_diagoanal = [matrix[x][rows - x - 1] for x in range(rows)]

print(f"""Primary diagonal: {', '.join(map(str, primary_diagoanal))}. Sum: {sum(primary_diagoanal)}
Secondary diagonal: {', '.join(map(str, secondary_diagoanal))}. Sum: {sum(secondary_diagoanal)}""")