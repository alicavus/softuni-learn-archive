numbers = [int(x) for x in input().strip().split(", ")]

count_of_beggars = int(input())

beggars_outcome = []

for beggar in range(count_of_beggars):
    beggars_outcome.append(sum(numbers[beggar::count_of_beggars]))

print(beggars_outcome)
