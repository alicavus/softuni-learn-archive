from pathlib import  Path

filepath = Path('numbers.txt')

try:
    file = open(filepath, 'r')
except FileNotFoundError:
    pass
else:
    for line in file:
        print(line, end='')