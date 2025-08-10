from collections import deque


circle = deque(input().split())
toss_number = int(input())

while len(circle) > 1:
    for toss_idx in range(1, toss_number+1):
        circle.append(circle.popleft())
    print(f"Removed {circle.pop()}")


print(f"Last is {circle.pop()}")