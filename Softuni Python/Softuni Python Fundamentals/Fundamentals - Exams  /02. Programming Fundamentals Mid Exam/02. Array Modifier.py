
my_integers = [int(x) for x in input().strip().split(" ")]

while True:
    cmd_line = input().strip()

    if cmd_line == "end": break

    cmd_line_list = cmd_line.split(" ")

    command = cmd_line_list[0]

    if command == "decrease":
        for ix in range(len(my_integers)):
            my_integers[ix] -= 1
    
    else:
        index1 = int(cmd_line_list[1])
        index2 = int(cmd_line_list[2])

        if command == "swap":
            buf = my_integers[index1]
            my_integers[index1] = my_integers[index2]
            my_integers[index2] = buf
        
        elif command == "multiply":
            my_integers[index1] = my_integers[index1] * my_integers[index2]

    

print(", ".join([str(x) for x in my_integers]))