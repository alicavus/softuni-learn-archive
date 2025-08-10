def accommodate_new_pets(available_capacity: int, maximum_weight: float, *args: (str, float)) -> str:
    accommodated = {}
    has_failed = True

    for pet_data in args:
        if available_capacity == 0:
            break
        pet_type, pet_weight = pet_data

        if pet_weight > maximum_weight:
            continue

        if pet_type not in accommodated:
            accommodated[pet_type] = 0

        accommodated[pet_type] += 1
        available_capacity -= 1

    else:
        has_failed = False

    result = [f"All pets are accommodated! Available capacity: {available_capacity}." if not has_failed else "You did not manage to accommodate all pets!"]

    result += [f"Accommodated pets:"]

    for pet_data in sorted(accommodated.items(), key=lambda x: x[0]):
        result += [f"{pet_data[0]}: {pet_data[1]}"]

    return "\n".join(result)

print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))


