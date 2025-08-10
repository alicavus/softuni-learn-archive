set_one, set_two = set(), set()

set_one_size, set_two_size = map(int, input().split())

for _ in range(set_one_size):
    set_one.add(int(input()))

for _ in range(set_two_size):
    set_two.add(int(input()))

intersection = set_one.intersection(set_two)

for elem in intersection:
    print(elem)