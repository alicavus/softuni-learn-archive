numbers_count = int(input())

numbers = [int(input()) for _ in range(numbers_count)]

output = []

match input():
    case 'even':
        output = [x for x in numbers if not x % 2]
    case 'odd':
        output = [x for x in numbers if x % 2]
    case 'negative':
        output = [x for x in numbers if x < 0]
    case 'positive':
        output = [x for x in numbers if x >= 0]
    case _:
        pass

print(output)
