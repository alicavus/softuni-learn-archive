numbers = [int(x) for x in input()]

numbers.sort(reverse=True)

print("".join([str(x) for x in numbers]))
