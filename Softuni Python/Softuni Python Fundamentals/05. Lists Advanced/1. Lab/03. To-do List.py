
my_todo_list = [None] * 11

while True:
    command_line = input()
    
    if command_line == "End":
        print([x for x in my_todo_list if x is not None])
        break

    importance_list = command_line.split('-', 1)

    importance = int(importance_list[0])
    task = importance_list[1]

    my_todo_list[importance] = task



