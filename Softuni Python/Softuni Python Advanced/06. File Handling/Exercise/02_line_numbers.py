# Exercise: File Handling
# Task 2. Line Numbers

from pathlib import Path as p
from string import ascii_letters, punctuation


def counter(text: str) -> tuple[int, int]:
    letters, punctuations = 0, 0
    for char in text:
        if char in ascii_letters:
            letters += 1
        elif char in punctuation:
            punctuations += 1
    return letters, punctuations

def pretty_counter(*args) -> str:
    args = [str(x) for x in args]
    return f'({")(".join(args)})'


input_file_path = p(__file__.replace(".py", "_input.txt"))
output_file_path = p(__file__.replace(".py", "_output.txt"))

try:
    with output_file_path.open("w") as output_file:
        with input_file_path.open("r") as input_file:
            for cnt, line in enumerate(input_file, 1):
                output_file.write(f"Line {cnt}: {line.rstrip('\n')} " + pretty_counter(*counter(line)) + "\n")
except Exception as e:
    print(*e.args)



