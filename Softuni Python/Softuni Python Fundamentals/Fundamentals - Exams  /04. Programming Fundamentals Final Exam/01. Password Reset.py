curr_password = input()

while True:
    command_line = input()

    if command_line == "Done":
        print(f"Your password is: {curr_password}")
        break

    commands = command_line.split()

    match commands[0]:
        case "TakeOdd":
            curr_password = curr_password[1::2]
            print(curr_password)

        case "Cut":
            index, length = list(map(int, commands[1:]))
            curr_password = curr_password[:index] + curr_password[index+length:]
            print(curr_password)
        
        case "Substitute":
            substring, substitute = commands[1:]

            if substring in curr_password:
                curr_password = curr_password.replace(substring, substitute)
                print(curr_password)
            else:
                print("Nothing to replace!")