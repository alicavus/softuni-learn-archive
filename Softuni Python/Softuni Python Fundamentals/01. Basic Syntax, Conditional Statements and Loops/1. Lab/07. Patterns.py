number = int(input())

for n in range(number + 1):
    for _ in range(n):
        print("*", end="")
    print()

for n in range(number-1, 0, -1):
    for _ in range(n):
        print("*", end="")
    print()
