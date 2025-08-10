number_of_wagons = int(input())

train = [0] * number_of_wagons

while True:
    command_line = input()

    if command_line == "End":
        print(train)
        break

    commands = command_line.split()
    command = commands[0]

    match command:
        case "add":
            count_of_people = int(commands[1])
            train[-1] += count_of_people
        
        case "insert" | "leave":
            index, count_of_people = int(commands[1]), int(commands[2])
            train[index] += count_of_people if command == "insert" else -count_of_people

