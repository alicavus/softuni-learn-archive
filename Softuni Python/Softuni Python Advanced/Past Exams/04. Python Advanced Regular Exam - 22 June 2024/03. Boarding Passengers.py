def boarding_passengers(ship_capacity: int, *args: tuple[int, str]) -> str:
    boarded = {}
    is_partial = False

    for boarding_data in args:
        group_count, group_program = boarding_data

        if ship_capacity == 0:
            is_partial = True
            break

        elif group_count > ship_capacity:
            is_partial = True
            continue

        ship_capacity -= group_count

        if group_program not in boarded:
            boarded[group_program] = 0

        boarded[group_program] += group_count

    result = ["Boarding details by benefit plan:"]

    for boarding_data in sorted(boarded.items(), key=lambda item: (-item[1], item[0])):
        result += [f"## {boarding_data[0]}: {boarding_data[1]} guests"]

    if not is_partial:
        result += [f"All passengers are successfully boarded!"]
    elif ship_capacity == 0:
        result += [f"Boarding unsuccessful. Cruise ship at full capacity."]
    else:
        result += [f"Partial boarding completed. Available capacity: {ship_capacity}."]

    return "\n".join(result)


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
