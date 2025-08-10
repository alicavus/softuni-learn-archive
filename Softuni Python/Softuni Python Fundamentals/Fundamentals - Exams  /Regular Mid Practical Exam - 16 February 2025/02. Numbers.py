numbers = input().split()

while True:
    commands = input().split()

    if commands[0] == "Finish":
        print(" ".join(numbers))
        break

    match commands[0]:
        case "Add":
            numbers.append(commands[1])
        case "Remove":
            numbers.remove(commands[1])
        case "Replace":
            value, replacement = commands[1:]
            if value in numbers:
                numbers[numbers.index(value)] = replacement
        case "Collapse":
            for idx in range(len(numbers)-1, -1, -1):
                if int(numbers[idx]) < int(commands[1]):
                    numbers.pop(idx)

