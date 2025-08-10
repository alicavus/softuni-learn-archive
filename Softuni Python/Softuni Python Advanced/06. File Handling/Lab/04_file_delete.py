from pathlib import Path

filepath = Path('my_first_file.txt')

if not filepath.exists():
    print('File already deleted!')

try:
    filepath.unlink()
except PermissionError:
    print('Permission denied!')

