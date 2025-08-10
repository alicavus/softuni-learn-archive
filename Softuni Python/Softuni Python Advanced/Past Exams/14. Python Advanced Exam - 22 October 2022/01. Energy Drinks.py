from collections import deque

caffeines = [int(x) for x in input().split(", ")]
energy_drink = deque([int(x) for x in input().split(", ")])

STAMATS_MAX_CAFFEINE_INTAKE = 300
STAMATS_REDUCE_CAFFEINE_AMOUNT = 30

stamats_caffeine_intake = 0

while caffeines and energy_drink:
    cur_caffeine = caffeines.pop()
    cur_energy_drink = energy_drink.popleft()

    cur_multiplication = cur_caffeine * cur_energy_drink

    if cur_multiplication + stamats_caffeine_intake <= STAMATS_MAX_CAFFEINE_INTAKE:
        stamats_caffeine_intake += cur_multiplication

    else:
        energy_drink.append(cur_energy_drink)

        stamats_caffeine_intake -= STAMATS_REDUCE_CAFFEINE_AMOUNT
        if stamats_caffeine_intake < 0:
            stamats_caffeine_intake = 0


if energy_drink:
    print("Drinks left:", ", ".join(map(str, energy_drink)))

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamats_caffeine_intake} mg caffeine.")



