from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

wasted_water = 0

while cups and bottles:
    current_cup = cups[0]
    current_bottle = bottles.pop()


    while current_cup > current_bottle and bottles:
        current_bottle += bottles.pop()
        
    wasted_water += current_bottle - current_cup
    cups.popleft()
else:
    if not cups:
        print(f"Bottles: {' '.join(reversed(list(map(str, bottles))))}")
    elif not bottles:
        print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted_water}")
        



