username = input()

command_line = input()

while command_line != "Registration":
    commands = command_line.split(" ")

    command = commands[0]

    if command == "Letters":
        if commands[1] == "Lower":
            username = username.lower()
        elif commands[1] == "Upper":
            username = username.upper()
        print(username)
        
    elif command == "Reverse":
        start_idx = int(commands[1])
        end_idx = int(commands[2])
        if not 0 <= start_idx <= end_idx < len(username):
            print(username[start_idx:end_idx+1][::-1])
    
    elif command == "Substring":
        substr = commands[1]
        if username.find(substr) != -1:
            print(username.replace(substr, ""))
        else:
            print(f"The username {username} doesn't contain {substr}.")
    
    elif command == "Replace":
        character = commands[1]
        username = username.replace(character, "-")
        print(username)
    
    elif command == "IsValid":
        character = commands[1]
        if username.find(character) != -1:
            print("Valid username.")
        else:
            print(f"{character} must be contained in your username.")
    
    command_line = input()
