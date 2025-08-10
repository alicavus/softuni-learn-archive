from math import ceil

numbers = [int(x) for x in input().split(", ")]
groups = []

for upper_boundary in range(1, ceil(max(numbers) / 10) + 1):
    group = [x for x in numbers if (upper_boundary - 1) * 10 <= x <= upper_boundary * 10]
    groups += [group]

for idx, group in enumerate(groups, 1):
    print(f"Group of {idx * 10}'s: {group}")

