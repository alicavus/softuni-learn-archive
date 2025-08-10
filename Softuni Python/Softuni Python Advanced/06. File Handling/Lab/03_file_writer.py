from pathlib import Path

try:
    filepath = Path('my_first_file.txt')
    file = open(filepath, 'x')
    file.write('I just created my first file!')
except FileExistsError:
    pass
finally:
    file.close()

