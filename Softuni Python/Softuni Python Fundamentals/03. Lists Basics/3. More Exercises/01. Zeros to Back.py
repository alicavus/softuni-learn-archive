def are_zeroes_back(l: list) -> bool:
    if 0 in l:
        return all(n == 0 for n in l[l.index(0):])
    
    return True

numbers = [int(x) for x in input().strip().split(', ')]

while not are_zeroes_back(numbers):
    numbers.remove(0)
    numbers.append(0)

print(numbers)
