age = int(input())

drink = 'toddy' if age <= 14 else 'coke' if age <= 18 else 'beer' if age <= 21 else 'whisky'

print(f'drink {drink}')