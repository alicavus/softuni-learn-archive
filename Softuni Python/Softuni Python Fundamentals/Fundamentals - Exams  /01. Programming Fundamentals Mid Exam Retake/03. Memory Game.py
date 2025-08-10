
sequence_of_numbers = [x for x in input().strip().split(" ")]

number_of_moves = 0

while True:
    command = input().strip()
    
    if command == "end": break

    if not len(sequence_of_numbers): continue

    number_of_moves += 1

    two_indexes = [int(x) for x in command.split(" ")]

    first_index = two_indexes[0]
    second_index =  two_indexes[1]

    if first_index == second_index or not all([x in range(len(sequence_of_numbers)) for x in two_indexes]):
        print("Invalid input! Adding additional elements to the board")
        index_to_insert = len(sequence_of_numbers) // 2
        sequence_of_numbers.insert(index_to_insert, f"-{number_of_moves}a")
        sequence_of_numbers.insert(index_to_insert, f"-{number_of_moves}a")
        continue
    
    if sequence_of_numbers[first_index] == sequence_of_numbers[second_index]:
        print(f"Congrats! You have found matching elements - {sequence_of_numbers[first_index]}!")
        sequence_of_numbers.pop(first_index if first_index > second_index else second_index)
        sequence_of_numbers.pop(first_index if first_index < second_index else second_index)
    
    else:
        print("Try again!")

if len(sequence_of_numbers):
    print(f"""Sorry you lose :(
{' '.join(sequence_of_numbers)}""")
else: print(f"You have won in {number_of_moves} turns!")

