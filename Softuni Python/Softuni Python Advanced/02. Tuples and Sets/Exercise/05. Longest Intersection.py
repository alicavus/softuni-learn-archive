from re import split

longest_intersection = []

for _ in range(int(input())):
    range_data = tuple(map(int, split('[,-]', input())))

    first_range = set(range(range_data[0], range_data[1]+1))
    second_range = set(range(range_data[2], range_data[3]+1))

    intersect = first_range.intersection(second_range)

    if len(intersect) > len(longest_intersection):
        longest_intersection = intersect


print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")