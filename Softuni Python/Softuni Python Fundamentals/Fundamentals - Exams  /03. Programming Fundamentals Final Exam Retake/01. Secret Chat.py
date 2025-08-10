concealed_message = input()

message = concealed_message

while True:
    command_line = input()

    if command_line == "Reveal":
        print(f"You have a new text message: {message}")
        break

    commands = command_line.split(":|:")

    match commands[0]:
        case "InsertSpace":
            index = int(commands[1])
            message = message[:index] + " " + message[index:]
        case "Reverse":
            substring = commands[1]

            if substring not in message:
                print("error")
                continue

            message = message.replace(substring, "", 1) + substring[::-1]
        
        case "ChangeAll":
            substring, replacement = commands[1:]
            message = message.replace(substring, replacement)
    
    print(message)


