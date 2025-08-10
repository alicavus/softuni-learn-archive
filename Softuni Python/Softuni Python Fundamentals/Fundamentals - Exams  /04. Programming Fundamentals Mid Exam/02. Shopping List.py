groceries = input().split("!")

while True:
    command_line = input()

    if command_line == "Go Shopping!":
        print(", ".join(groceries))
        break

    commands = command_line.split()

    if commands[0] == "Urgent":
        item = commands[1]
        if item in groceries:
            continue
        groceries = [item] + groceries

    elif commands[0] == "Unnecessary":
        item = commands[1]
        if item in groceries:
            groceries.remove(item)

    elif commands[0] == "Correct":
        old_item, new_item = commands[1:]

        if old_item in groceries:
            groceries = list(map(lambda x: x if x != old_item else new_item, groceries))

    elif commands[0] == "Rearrange":
        item = commands[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

    
    

