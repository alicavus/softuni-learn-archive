from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

matches = 0
not_fitted = len(worms)

while worms and holes:
    cur_worm = worms.pop()
    cur_hole = holes.popleft()

    if cur_worm != cur_hole:
        cur_worm -= 3
        if cur_worm > 0:
            worms.append(cur_worm)

    else:
        not_fitted -= 1
        matches += 1

print(f"Matches: {matches}" if matches else "There are no matches.")

if not not_fitted:
    print("Every worm found a suitable hole!")
elif not worms:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join(map(str, worms))}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(map(str, holes))}")