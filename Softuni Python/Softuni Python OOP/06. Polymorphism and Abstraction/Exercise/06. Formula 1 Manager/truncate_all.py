from os import walk, path
from pathlib import Path

msg = "Dou you want to reset all files in current directory?\nWrite 'Yes, I want this!' to procede:\n"

if input(msg) != 'Yes, I want this!':
    exit(0)

for dirpath, _, files in walk(top=Path(__file__).parent.absolute()):
    for file in files:
        cur_file = path.join(dirpath, file)
        if cur_file == __file__:
            continue
        with open(cur_file, "w") as f:
            pass

