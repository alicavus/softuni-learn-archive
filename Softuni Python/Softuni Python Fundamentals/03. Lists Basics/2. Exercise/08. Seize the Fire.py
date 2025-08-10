fire_level_info = input()

water = int(input())

total_effort = 0.0
total_fire = 0

valid_cells = []

for cell_info in fire_level_info.split('#'):
    if " = " not in cell_info or cell_info.index(" = ") in [0, len(cell_info) - 3] :
        continue

    cell_info_list = cell_info.split(" = ")

    if len(cell_info_list) != 2:
        continue

    type_of_fire = cell_info_list[0]
    cell_value = int(cell_info_list[1])

    match type_of_fire:
        case "High":
            if not 81 <= cell_value <= 125:
                continue
        case "Medium":
            if not 51 <= cell_value <= 80:
                continue
        case "Low":
            if not 1 <= cell_value <= 50:
                continue
        case _:
            continue
    
    if water < cell_value:
        continue

    water -= cell_value

    total_effort += cell_value / 4
    total_fire += cell_value

    valid_cells.append(f" - {cell_value}")


print("Cells:")
for cell in valid_cells:
    print(cell)
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")



