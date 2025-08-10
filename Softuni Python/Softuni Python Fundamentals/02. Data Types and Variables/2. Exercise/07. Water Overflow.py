TANK_CAPACITY = 255

water_in_tank = 0

for _ in range(int(input())):
    water = int(input())
    if water + water_in_tank > TANK_CAPACITY:
        print("Insufficient capacity!")
        continue
    water_in_tank += water

print(water_in_tank)
    