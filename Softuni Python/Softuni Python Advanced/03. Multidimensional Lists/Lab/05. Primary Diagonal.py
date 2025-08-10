matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

print(sum([matrix[idx][idx] for idx in range(len(matrix))]))