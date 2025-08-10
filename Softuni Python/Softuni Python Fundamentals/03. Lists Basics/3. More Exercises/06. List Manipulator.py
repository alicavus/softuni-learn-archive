sequence_of_numbers = [int(x) for x in input().strip().split(' ')]

while True:
    command_line_arguments = input().strip().split(' ')
    command = command_line_arguments[0]

    if command == 'end':
        print(sequence_of_numbers)
        break

    elif command == 'exchange':
        idx = int(command_line_arguments[1])
        if idx not in range(len(sequence_of_numbers)):
            print('Invalid index')
            continue
        sequence_of_numbers = sequence_of_numbers[idx+1:] + sequence_of_numbers[:idx+1]

    elif command in ['max', 'min']:
        el_type = command_line_arguments[1]

        l = []
        if el_type == 'odd':
            l = [x for x in sequence_of_numbers if x % 2]
        elif el_type == 'even':
            l = [x for x in sequence_of_numbers if not x % 2]
        
        res = None if len(l) == 0 else max(l) if command == 'max' else min(l)
       
        if res in sequence_of_numbers:
            idx = sequence_of_numbers.index(res)
            while res in sequence_of_numbers[idx+1:]:
                idx = sequence_of_numbers.index(res, idx+1)
            print(idx)
        else:
            print('No matches')
    
    elif command in ['first', 'last']:
        count = int(command_line_arguments[1])
        el_type = command_line_arguments[2]
        l = [x for x in sequence_of_numbers if x % 2] if el_type == 'odd' else [x for x in sequence_of_numbers if not x % 2] if el_type == 'even' else []
        l = l[:count] if command == 'first' else l[-count:] if command == 'last' else []
        if count in range(len(sequence_of_numbers)+1):
            print(l)
        else:
            print('Invalid count')