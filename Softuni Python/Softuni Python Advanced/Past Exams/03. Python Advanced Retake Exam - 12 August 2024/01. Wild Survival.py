from collections import deque

bees = deque([int(x) for x in input().split()])
bee_eaters = [int(x) for x in input().split()]

EATER_KILL_COUNT = 7

while bees and bee_eaters:
    current_bees = bees.popleft()
    current_eaters = bee_eaters.pop()

    while current_bees > 0 and current_eaters > 0:
        current_bees -= EATER_KILL_COUNT
        if current_bees >= 0:
            current_eaters -= 1
    
    if current_eaters > 0:
        bee_eaters.append(current_eaters)
    
    elif current_bees > 0:
        bees.append(current_bees)


print('The final battle is over!')

if not bees and not bee_eaters:
    print('But no one made it out alive!')
elif bees:
    print(f'Bee groups left: {", ".join(map(str, bees))}')
elif bee_eaters:
    print(f'Bee-eater groups left: {", ".join(map(str, bee_eaters))}')
