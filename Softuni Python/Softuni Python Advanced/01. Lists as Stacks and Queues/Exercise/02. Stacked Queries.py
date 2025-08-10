from collections import deque

stack = deque()

number_of_lines = int(input())

for _ in range(number_of_lines):
    query = input()

    if query.startswith("1 "):
        number = query.split()[1]
        stack.appendleft(int(number))
    elif query == "2":
        if(len(stack)):
            stack.popleft()
    elif query == "3":
        if len(stack):
            print(max(stack))
    elif query == "4":
        if len(stack):
            print(min(stack))

print(", ".join([str(x) for x in stack]))