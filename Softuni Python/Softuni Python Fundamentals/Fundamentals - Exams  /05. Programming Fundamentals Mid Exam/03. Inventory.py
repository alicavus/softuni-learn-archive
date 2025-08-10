my_items = input().split(", ")

while True:
    command_line = input()

    if command_line == "Craft!":
        print(", ".join(my_items))
        break

    commands = command_line.split(" - ")

    if commands[0] == "Collect":
        if commands[1] not in my_items:
            my_items += [commands[1]]

    elif commands[0] == "Drop":
        if commands[1] in my_items:
            my_items.remove(commands[1])

    elif commands[0] == "Combine Items":
        items = commands[1].split(":")

        if items[0] in my_items:
            idx = my_items.index(items[0])
            my_items.insert(idx+1, items[1])

    elif commands[0] == "Renew":
        if commands[1] in my_items:
            my_items.remove(commands[1])
            my_items += [commands[1]]
        
        
