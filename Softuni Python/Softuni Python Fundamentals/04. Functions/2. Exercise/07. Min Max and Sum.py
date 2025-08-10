def minimum_maximum_sum(l: list):
    print(f"The minimum number is {min(l)}\n", f"The maximum number is {max(l)}\n", f"The sum number is: {sum(l)}", sep="")

numbers = [int(x) for x in input().strip().split()]

minimum_maximum_sum(numbers)