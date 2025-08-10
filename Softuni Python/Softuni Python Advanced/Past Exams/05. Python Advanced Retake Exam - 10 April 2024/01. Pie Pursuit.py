from collections import deque

contestants = deque([int(x) for x in input().split()])
pies = [int(x) for x in input().split()]

while contestants and pies:
    current_contestant = contestants.popleft()
    current_pie = pies.pop()

    if current_contestant > current_pie:
        current_contestant -= current_pie
        contestants.append(current_contestant)

    elif current_contestant < current_pie:
        current_pie -= current_contestant
        if pies and current_pie == 1:
            pies[-1] += 1

        else:
            pies.append(current_pie)

if not contestants and not pies:
    print("We have a champion!")

elif contestants:
    print("We will have to wait for more pies to be baked!")
    print("Contestants left:", ", ".join(map(str, contestants)))

else:
    print("Our contestants need to rest!")
    print("Pies left:", ", ".join(map(str, pies)))
