from collections import deque
milligrams_caffeine = list(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))

stamat_caffeine = 0

while True:
    if not milligrams_caffeine:
        break
    if not energy_drinks:
        break
    current_milligrams_caffeine = milligrams_caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    caffeine = current_milligrams_caffeine * current_energy_drink
    if caffeine + stamat_caffeine <= 300:
        stamat_caffeine += caffeine
    else:
        energy_drinks.append(current_energy_drink)
        stamat_caffeine -= 30
        if stamat_caffeine < 0:
            stamat_caffeine = 0


if energy_drinks:
    print(f"Drinks left: { ', '.join(map(str, energy_drinks)) }")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")