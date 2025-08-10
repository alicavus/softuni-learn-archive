cities = {}

while True:
    city_info = input()
    if city_info == "Sail":
        break
    name, population, gold = city_info.split("||")
    if name not in cities.keys():
        cities[name] = {
            "population": 0,
            "gold": 0
        }
    cities[name]["population"] += int(population)
    cities[name]["gold"] += int(gold)

while True:
    events_info = input()

    if events_info == "End":
        break

    events_data = events_info.split("=>")

    if events_data[0] == "Plunder":
        town, people, gold = events_data[1:]
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]["population"] -= int(people)
        cities[town]["gold"] -= int(gold)

        if cities[town]["population"] <= 0 or cities[town]["gold"] <= 0:
            print(f"{town} has been wiped off the map!")
            cities.pop(town)
    elif events_data[0] == "Prosper":
        town, gold = events_data[1:]
        gold = int(gold)

        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        cities[town]["gold"] += gold
        print(f'{gold} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')
        

if cities != {}:
    print(f"Ahoy, Captain! There are {len(cities.keys())} wealthy settlements to go to:")
    print("\n".join([f'{town} -> Population: {cities[town]["population"]} citizens, Gold: {cities[town]["gold"]} kg' for town in cities.keys()]))
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")