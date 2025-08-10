from collections import deque

bees = deque([int(b) for b in input().split()])
bee_eaters = [int(e) for e in input().split()]  # stack

while bees and bee_eaters:
    current_bees = bees.popleft()
    current_bee_eaters = bee_eaters.pop()

    # Fight until one of the groups is defeated
    while current_bees > 0 and current_bee_eaters > 0:
        if current_bee_eaters * 7 <= current_bees:
            current_bees -= current_bee_eaters * 7
            current_bee_eaters = 0
        else:
            current_bee_eaters -= (current_bees // 7)
            current_bees = 0

    # Post-fight outcomes
    if current_bees > 0 and current_bee_eaters == 0:
        bees.append(current_bees)
    elif current_bees == 0 and current_bee_eaters > 0:
        bee_eaters.append(current_bee_eaters)
    # If both groups are defeated, no action needed - they are already popped out

# Output result
print("The final battle is over!")
if not bees and not bee_eaters:
    print("But no one made it out alive!")
elif bees:
    print(f"Bee groups left: {', '.join(map(str, bees))}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters))}")

