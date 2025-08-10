matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]

flattened = [x for row in matrix for x in row]

print(flattened)