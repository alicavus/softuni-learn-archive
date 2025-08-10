from collections import deque

def create_unique():
    res = deque()
    for number in input().split():
        if number not in res:
            res.append(number)
    
    return res

def add_unique(numbers: deque, to_add: str):
    for number in to_add.split()[2:]:
        if number not in numbers:
            numbers.append(number)

def remove(numbers: deque, to_remove: str):
    for number in to_remove.split()[2:]:
        if number in numbers:
            numbers.remove(number)


numbers_one = create_unique()
numbers_two = create_unique()

for _ in range(int(input())):
    command = input()

    if command.startswith("Add First "):
        add_unique(numbers_one, command)

    elif command.startswith("Add Second "):
        add_unique(numbers_two, command)
    
    elif command.startswith("Remove First "):
        remove(numbers_one, command)
    
    elif command.startswith("Remove Second "):
        remove(numbers_two, command)
    
    elif command == "Check Subset":
        numbers_one_set = set(numbers_one)
        numbers_two_set = set(numbers_two)

        print(numbers_one_set.issubset(numbers_two_set) or numbers_one_set.issuperset(numbers_two_set))


print(", ".join(sorted(numbers_one, key=int)))
print(", ".join(sorted(numbers_two, key=int)))


