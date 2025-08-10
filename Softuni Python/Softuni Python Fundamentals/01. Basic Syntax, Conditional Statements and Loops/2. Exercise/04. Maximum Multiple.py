divisor = int(input())
boundary = int(input())

while boundary % divisor:
    boundary -= 1

print(boundary)
