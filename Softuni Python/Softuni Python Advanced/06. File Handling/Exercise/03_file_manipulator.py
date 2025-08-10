# Exercise: File Handling
# Task 3. File Manipulator

from pathlib import Path

def delete(obj: Path):
    '''Tries to delete filesystem object like file or directory.'''
    if obj.exists():
        try:
            if obj.is_dir():
                for item in obj.iterdir():
                    delete(item)
                obj.rmdir()
            else:
                obj.unlink()
        except Exception as e:
            print(*e.args)

def create(file: Path):
    '''Tries to create a new regular file.
    If there is a filesystem object it will be erased'''
    try:
        if file.exists():
            delete(file)
        file.touch()
    except Exception as e:
            print(*e.args)

def append_content(file: Path, content: str):
    '''Appends content to a regular file.'''
    try:
        if not file.exists():
            file.touch()
        elif not file.is_file():
            delete(file)
            file.touch()
        with open(file, "a") as f:
            f.write(content + "\n")
    except Exception as e:
            print(*e.args)

def replace_content(file: Path, old: str, new: str):
    '''Replaces all occurrences of old to new in target file.'''
    try:
        if not file.exists():
            return

        with file.open("r+") as source:
            txt = source.read()
            txt = txt.replace(old, new)
            source.seek(0)
            source.write(txt)
            source.truncate()

    except Exception as e:
            print(*e.args)

END_COMMAND = "End"
COMMAND_SEPARATOR = "-"

while True:
    commands = input().split(COMMAND_SEPARATOR)

    if commands[0] == END_COMMAND:
        break

    match commands[0]:
        case "Create":
            file = Path(commands[1])
            create(file)
        case "Add":
            file_name, content = commands[1:]
            append_content(Path(file_name), content)
        case "Replace":
            file_name, old_string, new_string = commands[1:]
            file = Path(file_name)

            if not file.exists():
                print("An error occurred")

            else:
                replace_content(file, old_string, new_string)

        case "Delete":
            file = Path(commands[1])

            if not file.exists():
                print("An error occurred")

            else:
                delete(file)