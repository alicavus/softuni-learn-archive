MIN_EXCLUDED = 1
MAX_EXCLUDED = 100
while True:
    number = float(input())
    if number >= MIN_EXCLUDED and number <= MAX_EXCLUDED:
        print(f'The number {number} is between 1 and 100')
        break
