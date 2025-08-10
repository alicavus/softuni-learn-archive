# Exercise: File Handling
# Task 4. Directory Traversal

from pathlib import Path

path = input("Please enter a valid directory path to traverse:\n")

directory = Path(path)

report_file = Path("report.txt")

if not directory.exists():
    print(f"Directory {path} doesn't exist.")
elif not directory.is_dir():
    print(f"Directory {path} isn't a directory.")
    directory = directory.parent

files = {}

try:
    for file in directory.iterdir():
        if file.is_file():
            suffix = file.suffix.lower()
            if len(suffix):
                if suffix not in files:
                    files[suffix] = []
                files[suffix].append(file.name)
        elif file.is_dir():
            for sub_file in file.iterdir():
                if sub_file.is_file():
                    suffix = sub_file.suffix.lower()
                    if len(suffix):
                        if suffix not in files:
                            files[suffix] = []
                        files[suffix].append(sub_file.name)

    with report_file.open('w') as r:
        for suffix, files_data in sorted(files.items(), key=lambda item: item[0]):
            r.write(suffix + "\n")
            for file in sorted(files_data):
                r.write(f"- - - {file}\n")
except Exception as e:
    print(f"Error has occured:", *e.args)
