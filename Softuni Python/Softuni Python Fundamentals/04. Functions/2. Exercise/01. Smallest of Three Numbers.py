def find_smallest(a: int, b: int, c: int) -> int:
    return min(a, b, c)

a, b, c = [int(input()) for x in '123']

print(find_smallest(a=a, b=b, c=c))