number_one, number_two = [int(input()), int(input())]

max_number = max(number_one, number_two)
min_number = min(number_one, number_two)

res = 1

for multiplier in range(max_number, min_number, -1):
    res *= multiplier

print(f'{res:.2f}' if number_one >= number_two else f'{1 / res:.2f}')