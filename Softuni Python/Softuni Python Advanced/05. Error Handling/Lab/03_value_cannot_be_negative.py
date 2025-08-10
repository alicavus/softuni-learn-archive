class ValueCannotBeNegative(Exception):
    pass

COUNT_NUMBERS = 5

for _ in range(COUNT_NUMBERS):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative