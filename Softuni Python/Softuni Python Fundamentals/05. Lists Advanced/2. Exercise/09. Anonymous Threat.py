strings = input().split()

while True:
    command_line = input()

    if command_line == "3:1":
        print(" ".join(strings))
        break

    commands = command_line.split()

    if commands[0] == "merge":
        start_idx, end_idx = [int(x) for x in commands[1:]]
        
        if start_idx < 0 :
            start_idx = 0
        
        if end_idx > len(strings):
            end_idx = len(strings)
        
        strings = strings[:start_idx] + ["".join(strings[start_idx:end_idx+1])] + strings[end_idx+1:]

    if commands[0] == "divide":
        idx, partitions_cnt = [int(x) for x in commands[1:]]

        word_to_divide = strings[idx]

        len_of_word_to_divide = len(word_to_divide)
        len_of_substrings = len_of_word_to_divide // partitions_cnt

        divided_strings = []

        for curr_partition_idx in range(partitions_cnt):
            curr_substring_idx = curr_partition_idx * len_of_substrings
            next_substring_idx = (curr_partition_idx+1) * len_of_substrings
            if curr_partition_idx == partitions_cnt - 1:
                next_substring_idx = len_of_word_to_divide
            curr_substring = word_to_divide[curr_substring_idx:next_substring_idx]
            divided_strings += [curr_substring]
        
        strings = strings[:idx] + divided_strings + strings[idx+1:]


