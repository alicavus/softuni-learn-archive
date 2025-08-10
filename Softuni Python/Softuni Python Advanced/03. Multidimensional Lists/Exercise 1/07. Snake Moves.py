from collections import deque

rows, cols = map(int, input().split())

snake = deque(input())

field = []


for ridx in range(rows):
    row = [0] * cols
    for cidx in range(cols):
        ch = snake.popleft()
        snake.append(ch)
        row[cidx if ridx % 2 == 0 else cols - cidx - 1] = ch
            
    field.append(row)

for r in field:
    print(*r, sep="")