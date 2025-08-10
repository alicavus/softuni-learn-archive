# Exercise: File Handling
# Task 1. Even Lines

from pathlib import Path as p

input_file_path = p(__file__).with_suffix(".txt")
chars_to_replace = ["-", ",", ".", "!", "?"]
replace_char = "@"

try:
    with input_file_path.open('r') as input_file:
        content = input_file.readlines()
        for cur_line, line in enumerate(content):
            if cur_line % 2:
                continue
            for ch in chars_to_replace:
                line = line.replace(ch, replace_char)
            print(*reversed(line.split()))
except Exception as e:
    print(f"There was an error reading file:", *e.args)