from collections import deque

def which_duck(multipl: int) -> bool:
    global rubber_ducks

    for duck in rubber_ducks:
        if rubber_ducks[duck]["min"] <= multipl <= rubber_ducks[duck]["max"]:
            rubber_ducks[duck]["count"] += 1
            return True
    return False


time_for_task = deque([int(x) for x in input().split()])
number_of_tasks = [int(x) for x in input().split()]

rubber_ducks = {
    "Darth Vader Ducky": {"min": 0, "max": 60, "count": 0},
    "Thor Ducky": {"min": 0, "max": 120, "count": 0},
    "Big Blue Rubber Ducky": {"min": 121, "max": 180, "count": 0},
    "Small Yellow Rubber Ducky": {"min": 181, "max": 240, "count": 0}
}

while time_for_task and number_of_tasks:
    curr_time = time_for_task.popleft()
    curr_number = number_of_tasks.pop()

    curr_mult = curr_time * curr_number

    if not which_duck(curr_mult):
        time_for_task.append(curr_time)
        number_of_tasks.append(curr_number - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck in rubber_ducks:
    print(f"{duck}: {rubber_ducks[duck]['count']}")