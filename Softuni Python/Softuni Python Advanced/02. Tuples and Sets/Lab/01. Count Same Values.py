numbers = tuple(map(float, input().split()))

numbers_occurences = dict()

for number in numbers:
    if number not in numbers_occurences.keys():
        numbers_occurences[number] = 0
    numbers_occurences[number] += 1

for number, count in numbers_occurences.items():
    print(f"{number} - {count} times")