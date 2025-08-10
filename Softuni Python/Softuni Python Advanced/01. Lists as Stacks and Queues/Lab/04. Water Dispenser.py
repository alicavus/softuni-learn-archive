from collections import deque

dispencer = int(input())
queue = deque()

while True:
    name = input()

    if name == "Start":
        break

    queue.append(name)

while True:
    curr_action = input()
    
    if curr_action.isdigit():
        needed_water = int(curr_action)

        curr_person = queue.popleft()
        
        if needed_water <= dispencer:
            print(f"{curr_person} got water")
            dispencer -= needed_water
        
        else:
            print(f"{curr_person} must wait")
    
    elif curr_action.startswith("refill "):
        dispencer += int(curr_action.split()[1])

    elif curr_action == "End":
        print(f"{dispencer} liters left")
        break


