sequence_of_numbers = [int(x) for x in input().strip().split(' ')]
number = int(input())

number -= 1
executed = []

sequence_copy = sequence_of_numbers.copy()

while sorted(executed) != sorted(sequence_of_numbers):
    cur_number = number % len(sequence_copy)
    executed.append(sequence_copy[cur_number])
    sequence_copy = sequence_copy[cur_number+1:] + sequence_copy[:cur_number]

print(str(executed).replace(", ", ","))