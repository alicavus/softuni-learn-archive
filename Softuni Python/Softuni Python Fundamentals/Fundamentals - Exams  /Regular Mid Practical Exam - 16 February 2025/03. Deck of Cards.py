
separator = ", "
deck_of_cards = input().split(separator)

number_of_commands = int(input())

for _ in range(number_of_commands):
    commands = input().split(separator)

    match commands[0]:
        case "Add":
            if commands[1] not in deck_of_cards:
                deck_of_cards.append(commands[1])
                print("Card successfully added")
            else:
                print("Card is already in the deck")
        case "Remove":
            if commands[1] in deck_of_cards:
                deck_of_cards.remove(commands[1])
                print("Card successfully removed")
            else:
                print("Card not found")
        case "Remove At":
            index = int(commands[1])
            if index in range(len(deck_of_cards)):
                deck_of_cards.pop(index)
                print("Card successfully removed")
            else:
                print("Index out of range")
        case "Insert":
            index = int(commands[1])
            card_name = commands[2]
            if index in range(len(deck_of_cards)):
                if card_name in deck_of_cards:
                    print("Card is already added")
                else:
                    deck_of_cards.insert(index, card_name)
                    print("Card successfully added")
            else:
                print("Index out of range")

print(separator.join(deck_of_cards))