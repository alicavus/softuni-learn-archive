names = []

for _ in range(int(input())):
    names.append(input())

unique_names = set(names)

for unique_name in unique_names:
    print(unique_name)