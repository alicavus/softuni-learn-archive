def check_plant(plant: str) -> bool:
    global plants
    if plant not in plants:
        print("error")
        return False
    return True

plant_info_count = int(input())

plants = dict()

for _ in range(plant_info_count):
    
    plant, rarity = input().split("<->")

    plants[plant] = {"rarity": int(rarity), "rating": []}

while True:
    command_line = input()

    if command_line == "Exhibition":
        print("Plants for the exhibition:")
        for plant in plants:
            avg = 0.0
            for rate in plants[plant]["rating"]:
                avg += rate
            avg /= len(plants[plant]["rating"]) if len(plants[plant]["rating"]) else 1
            print(f"- {plant}; Rarity: {plants[plant]['rarity']}; Rating: {avg:.2f}")
        break

    commands = command_line.split(": ")

    match commands[0]:
        case "Rate":
            plant, rating = commands[1].split(" - ")

            if not check_plant(plant):
                continue

            plants[plant]["rating"].append(int(rating))
        
        case "Update":
            plant, new_rarity = commands[1].split(" - ")

            if not check_plant(plant):
                continue
            
            plants[plant]["rarity"] = int(new_rarity)
        
        case "Reset":
            plant = commands[1]

            if not check_plant(plant):
                continue

            plants[plant]["rating"] = []




