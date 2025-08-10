def plant_garden(available_space, *allowed_plants, **plant_requests):
    allowed_plants_data = {plant_type: space for plant_type, space in allowed_plants}
    planted_plants = {}

    # Process each requested plant type
    for plant_type, quantity in sorted(plant_requests.items()):
        if plant_type not in allowed_plants_data: # Check if the plant type is allowed
            continue
        space_per_plant = allowed_plants_data[plant_type]  # Get space required per plant
        max_possible_plants = int(available_space / space_per_plant)  # Calculate how many pcs can fit
        plants_to_plant = min(max_possible_plants, quantity)  # Determine how many pcs to plant

        if plants_to_plant > 0:
            planted_plants[plant_type] = plants_to_plant  # Record planted plants
            available_space -= plants_to_plant * space_per_plant  # Update available space
        if available_space <= 0.0:
            break

    result = ["Planted plants:"]
    [result.append(f"{plant_type}: {planted_plants[plant_type]}") for plant_type in sorted(planted_plants)]
    formated_planted_pcs = "\n".join(result)

    if all(planted_plants.get(pt, 0) == qty for pt, qty in plant_requests.items() if pt in allowed_plants_data):
        return f"All plants were planted! Available garden space: {available_space:.1f} sq meters.\n{formated_planted_pcs}"
    return f"Not enough space to plant all requested plants!\n{formated_planted_pcs}"
