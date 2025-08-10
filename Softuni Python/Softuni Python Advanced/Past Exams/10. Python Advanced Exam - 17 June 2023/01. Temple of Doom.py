from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    curr_tool = tools.popleft()
    curr_substance = substances.pop()

    curr_multiplication = curr_tool * curr_substance

    if curr_multiplication in challenges:
        challenges.remove(curr_multiplication)
    else:
        curr_tool += 1
        tools.append(curr_tool)
        curr_substance += -1
        if curr_substance:
            substances.append(curr_substance)


if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print("Tools:", ", ".join(map(str, tools)))

if substances:
    print("Substances:", ", ".join(map(str, substances)))

if challenges:
    print("Challenges:", ", ".join(map(str, challenges)))
