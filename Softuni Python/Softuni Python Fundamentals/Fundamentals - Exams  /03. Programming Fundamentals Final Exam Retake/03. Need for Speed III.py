number_of_cars = int(input())

fuel_tank_capacity = 75
max_mileage = 100_000
min_reset_mileage = 10_000

cars = dict()

for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

while True:
    command_line = input()

    if command_line == "Stop":
        for car, car_data in cars.items():
            print(f'{car} -> Mileage: {car_data["mileage"]} kms, Fuel in the tank: {car_data["fuel"]} lt.')
        break

    commands = command_line.split(" : ")

    match commands[0]:
        case "Drive":
            car, distance, fuel = commands[1:]
            distance = int(distance)
            fuel = int(fuel)

            if cars[car]["fuel"] < fuel:
                print("Not enough fuel to make that ride")
                continue

            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance

            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            
            if cars[car]["mileage"] >= max_mileage:
                cars.pop(car)
                print(f"Time to sell the {car}!")
        
        case "Refuel":
            car = commands[1]
            fuel = int(commands[2])

            max_fuel_to_refill = fuel_tank_capacity - cars[car]["fuel"]

            if fuel > max_fuel_to_refill:
                fuel = max_fuel_to_refill
            
            cars[car]["fuel"] += fuel

            print(f"{car} refueled with {fuel} liters")
        
        case "Revert":
            car = commands[1]
            mileage = int(commands[2])

            if cars[car]["mileage"] - mileage < min_reset_mileage:
                cars[car]["mileage"] = min_reset_mileage
                continue

            cars[car]["mileage"] -= mileage
            print(f"{car} mileage decreased by {mileage} kilometers")









