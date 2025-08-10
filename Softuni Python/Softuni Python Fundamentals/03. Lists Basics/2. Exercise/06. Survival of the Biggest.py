numbers  = [int(x) for x in input().strip().split(' ')]

for _ in range(int(input())):
    min_element = min(numbers)
    numbers.remove(min_element)

print(", ".join([str(x) for x in numbers]))