encrypted_message = input()

message = encrypted_message

while True:
    command_line = input()

    if command_line == "Decode":
        print(f"The decrypted message is: {message}")
        break

    commands = command_line.split("|")

    match commands[0]:
        case "Move":
            number_of_letters = int(commands[1])
            message = message[number_of_letters:] + message[:number_of_letters]
        case "Insert":
            index, value = commands[1:]
            index = int(index)
            message = message[:index] + value + message[index:]
        case "ChangeAll":
            substring, replacement = commands[1:] 
            message = message.replace(substring, replacement)