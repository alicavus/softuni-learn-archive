gifts = input().strip().split(' ')

while True:
    cmd_line = input()
    
    if cmd_line == "No Money":
        break

    command = cmd_line.split(' ')[0]

    gift = cmd_line.split(' ')[1]

    match command:
        case "OutOfStock":
            while gift in gifts:
                idx = gifts.index(gift)
                gifts[idx] = "None"
        case "Required":
            idx = int(cmd_line.split(' ')[2])
            if 0 <= idx < len(gifts):
                gifts[idx] = gift
        case "JustInCase":
            gifts[-1] = gift
        case _:
            pass

print(" ".join([gift for gift in gifts if gift != "None"]))