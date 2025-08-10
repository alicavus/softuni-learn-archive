from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque([int(x) for x in input().split()])
amount_of_fuel_needed = deque([int(x) for x in input().split()])

reached_altitude = 0

while initial_fuel and additional_consumption_index and amount_of_fuel_needed:
    current_fuel = initial_fuel.pop()
    current_additional_consumption = additional_consumption_index.popleft()

    subtracted_fuel = current_fuel - current_additional_consumption

    if subtracted_fuel >= amount_of_fuel_needed[0]:
        reached_altitude += 1
        amount_of_fuel_needed.popleft()
        print(f"John has reached: Altitude {reached_altitude}")

    else:
        print(f"John did not reach: Altitude {reached_altitude + 1}")
        break

if amount_of_fuel_needed:
    print("John failed to reach the top.")
    if reached_altitude:
        print(f"Reached altitudes: {', '.join([f'Altitude {altitude}' for altitude in range(1, reached_altitude + 1)])}")
    else:
        print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")