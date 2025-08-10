my_stops = input()

while True:
    command_line = input()

    if command_line == "Travel":
        print(f"Ready for world tour! Planned stops: {my_stops}")
        break

    commands = command_line.split(':')

    match commands[0]:
        case "Add Stop":
            idx, string = commands[1:]
            idx  = int(idx)

            if idx in range(len(my_stops)):
                my_stops = my_stops[:idx] + string + my_stops[idx:]
        
        case "Remove Stop":
            start_index, end_index = [int(x) for x in commands[1:]]

            if all([x in range(len(my_stops)) for x in [start_index, end_index]]):
                my_stops = my_stops[:start_index] + my_stops[end_index+1:]
        
        
        case "Switch":
            old_string, new_string = commands[1:]
            my_stops = my_stops.replace(old_string, new_string)

    print(my_stops)

