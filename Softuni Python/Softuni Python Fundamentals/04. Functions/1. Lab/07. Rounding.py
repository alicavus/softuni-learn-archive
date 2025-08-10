def round_numbers(numbers: list) -> list:
    return [round(x) for x in numbers]

print(round_numbers([float(x) for x in input().strip().split(' ')]))