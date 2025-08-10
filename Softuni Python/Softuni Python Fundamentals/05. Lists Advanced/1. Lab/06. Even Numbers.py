numbers = enumerate(input().split(", "))

print([idx for idx, val in numbers if not int(val) % 2])

