parking = {}

for _ in range(int(input())):
    command_line = input()

    commands = command_line.split()

    match commands[0]:
        case "register":
            user, plate = commands[1:]

            if user in parking:
                print(f"ERROR: already registered with plate number {parking[user]}")
            
            else:
                parking[user] = plate
                print(f"{user} registered {parking[user]} successfully")
    
        case "unregister":
            user = commands[1]

            if user not in parking:
                print(f"ERROR: user {user} not found")
            
            else:
                parking.pop(user)
                print(f"{user} unregistered successfully")

for user in parking:
    print(f"{user} => {parking[user]}")