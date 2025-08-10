def sum_numbers(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def add_and_subtract(a: int, b: int, c: int) -> int:
    print(subtract(sum_numbers(a, b), c))

a, b, c = [int(input()) for x in range(3)]

add_and_subtract(a=a, b=b, c=c)
