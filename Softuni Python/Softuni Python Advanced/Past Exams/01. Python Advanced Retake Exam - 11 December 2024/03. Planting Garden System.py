def plant_garden(garden_space: float, *args, **kwargs) -> str:
    def plant_flower(flower_name:str, flower_quantity: int):
        nonlocal planted
        if flower_name not in planted:
            planted[flower_name] = 0
        planted[flower_name] += flower_quantity
    
    planted = {}
    failed = False
    result = ""


    allowed_plants = {
        plant[0]: plant[1] for plant in args
    }

    kwargs = {
        flower_name:flower_quantity for flower_name, flower_quantity in kwargs.items() if flower_name in allowed_plants.keys()
    }
    
    for flower_data in sorted(kwargs.items(), key=lambda x: x[0]):
        flower_name, flower_quantity = flower_data

        area_needed = allowed_plants[flower_name] * flower_quantity

        if area_needed > garden_space:
            quantity = int(garden_space // allowed_plants[flower_name])

            if quantity > 0:
                plant_flower(flower_name, quantity)
                garden_space -= quantity * allowed_plants[flower_name]

            failed = True            
            continue

        garden_space -= area_needed
        plant_flower(flower_name, flower_quantity)
        
    if failed:
        result = "Not enough space to plant all requested plants!"
    else:
        result = f"All plants were planted! Available garden space: {garden_space:.1f} sq meters."
    
    result += "\nPlanted plants:"

    if planted:
        for plant_name, plant_quantity in planted.items():
            result += f"\n{plant_name}: {plant_quantity}"
    
    return result

print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))