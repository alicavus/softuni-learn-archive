from pathlib import Path
filename = "text.txt"


try:
    file = open(filename, "r")
    print('File found')
except FileNotFoundError:
    print('File not found')