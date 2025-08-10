from collections import deque

def next_drone(drones: dict, assembled: list, power: int) -> int:
    for p in drones:
        if p <= power and drones[p] not in assembled:
            return p
    return None

drones_power = {
    100: "Sentinel-X",
    85: "Viper-MKII",
    75: "Aegis-7",
    65: "Striker-R",
    55: "Titan-Core"
}

assembled_drones = []

mechanical_parts = [int(part) for part in input().split()]
power_cells = deque([int(cell) for cell in input().split()])

while mechanical_parts and power_cells and len(assembled_drones) != len(drones_power):
    curr_part = mechanical_parts.pop()
    curr_cell = power_cells.popleft()

    curr_power = curr_cell + curr_part

    if curr_power in drones_power and drones_power[curr_power] not in assembled_drones:
            assembled_drones += [drones_power[curr_power]]

    else:
        n_drone_power = next_drone(drones_power, assembled_drones, curr_power)

        if n_drone_power:
            assembled_drones += [drones_power[n_drone_power]]
            curr_cell -= 30

        else:
            curr_cell -= 1

        if curr_cell > 0:
            power_cells.append(curr_cell)
    

if len(assembled_drones) == len(drones_power):
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")

if assembled_drones:
    print(f"Assembled Drones: {', '.join(assembled_drones)}")

if mechanical_parts:
    print(f"Mechanical Parts: {', '.join(reversed([str(el) for el in mechanical_parts]))}")

if power_cells:
    print(f"Power Cells: {', '.join(map(str, power_cells))}")
