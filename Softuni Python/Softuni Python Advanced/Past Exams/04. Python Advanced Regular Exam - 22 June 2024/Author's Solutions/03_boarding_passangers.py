def boarding_passengers(capacity, *passenger_groups):
    # Initialize variables
    available_capacity = capacity
    boarding_details = {}

    # Board passengers
    for passengers, program in passenger_groups:
        if passengers <= available_capacity:
            if program not in boarding_details:
                boarding_details[program] = 0
            boarding_details[program] += passengers
            available_capacity -= passengers
        # Stop boarding if capacity is zero
        if available_capacity == 0:
            break

    # Sort the boarding details
    sorted_boarding_details = sorted(
        boarding_details.items(),
        key=lambda x: (-x[1], x[0])
    )

    # Prepare the result string
    result = "Boarding details by benefit plan:\n"
    for program, count in sorted_boarding_details:
        result += f"## {program}: {count} guests\n"

    # Determine the final message
    total_boarded = sum(boarding_details.values())
    total_passengers = sum(group[0] for group in passenger_groups)

    if total_boarded == total_passengers:
        result += "All passengers are successfully boarded!"
    elif available_capacity == 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        result += f"Partial boarding completed. Available capacity: {available_capacity}."

    return result
