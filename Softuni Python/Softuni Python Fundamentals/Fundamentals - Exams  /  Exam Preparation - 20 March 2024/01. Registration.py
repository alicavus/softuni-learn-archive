username = input()

while True:
    commands = input()
    if commands == "Registration": break

    cmd_list = commands.split(sep=' ')

    match cmd_list[0]:
        case "Letters":
            if cmd_list[1] == "Lower":
                username = username.lower()
            elif cmd_list[1] == "Upper":
                username = username.upper()
            print(username)
        case "Reverse":
            indexes = [int(cmd_list[1]), int(cmd_list[2])]
            is_valid = True
            for index in indexes:
                if index < 0 or index >= len(username):
                    is_valid = False
                    break
            if is_valid:
                r = ''
                for ind in range(indexes[1], indexes[0]-1, -1):
                    r += username[ind]
                print(r)
        case "Substring":
            subs = cmd_list[1]
            index = username.find(subs)

            print(username.replace(subs, '') if index >= 0 else f"The username {username} doesn't contain {subs}.")
        
        case "Replace":
            username = username.replace(cmd_list[1][0], "-")
            print(username)
        
        case "IsValid":
            print("Valid username." if username.find(cmd_list[1][0]) >=0 else f'{cmd_list[1][0]} must be contained in your username.')
        case _:
            pass