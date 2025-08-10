activation_key = input()

command = input()

while command != "Generate":
    commands = command.split(">>>");

    match commands[0]:
        case "Contains":
            substr = commands[1]
            if activation_key.find(substr) != -1:
                print(f"{activation_key} contains {substr}")
            else:
                print("Substring not found!")
            
        case "Flip":
            transform_kind = commands[1]
            start_idx = int(commands[2])
            end_idx = int(commands[3])

            new_activation_key = activation_key[:start_idx]
            new_activation_key += activation_key[start_idx:end_idx].lower() if transform_kind == "Lower" \
            else activation_key[start_idx:end_idx].upper() if transform_kind == "Upper" else activation_key[start_idx:end_idx]
            new_activation_key += activation_key[end_idx:]
            activation_key = new_activation_key

            print(activation_key)
        
        case "Slice":
            start_idx = int(commands[1])
            end_idx = int(commands[2])

            activation_key = activation_key[:start_idx] + activation_key[end_idx:]

            print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")