energy = 100
coins = 100

working_day_events = input().split("|")

for event in working_day_events:
    event_name = event.split("-")[0]
    event_value = int(event.split("-")[1])

    match event_name:
        case "rest":
            if energy + event_value > 100:
                event_value = 100 - energy
            energy += event_value

            print(f"You gained {event_value} energy.")
            print(f"Current energy: {energy}.")

        case "order":
            if energy >= 30:
               coins += event_value
               energy -= 30
               print(f"You earned {event_value} coins.")
            else:
                energy += 50
                print("You had to rest!")
        case _:
            if event_value > coins:
                print(f"Closed! Cannot afford {event_name}.")
                break

            coins -= event_value  
            print(f"You bought {event_name}.")
else:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")