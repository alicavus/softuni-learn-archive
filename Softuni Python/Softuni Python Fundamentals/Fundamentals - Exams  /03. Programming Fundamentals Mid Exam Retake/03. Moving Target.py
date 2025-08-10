sequence_of_targets = list(map(int, input().split()))

while True:
    command_line = input()

    if command_line == "End":
        print("|".join(map(str, sequence_of_targets)))
        break

    commands = command_line.split()

    match commands[0]:
        case "Shoot":
            index, power = list(map(int, commands[1:]))
            if index not in range(len(sequence_of_targets)):
                continue

            sequence_of_targets[index] -= power
            if sequence_of_targets[index] <= 0:
                sequence_of_targets.pop(index)

        case "Add":
            index, value = list(map(int, commands[1:]))
            if index not in range(len(sequence_of_targets)):
                print("Invalid placement!")
                continue
            sequence_of_targets.insert(index, value)
        
        case "Strike":
            index, radius = list(map(int, commands[1:]))
            if index-radius not in range(len(sequence_of_targets)) \
            or index+radius not in range(len(sequence_of_targets)):
                print("Strike missed!")
                continue
            else:
                for idx in range(index+radius, index-radius-1, -1):
                    sequence_of_targets.pop(idx)