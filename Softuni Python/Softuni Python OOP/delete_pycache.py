from pathlib import Path

def recursive_delete(folder: Path):
    deleted = []
    for d in folder.iterdir():
        if d.is_dir():
            deleted.extend(recursive_delete(d))
        else:
            deleted.append(str(d.resolve()))
            d.unlink()
    deleted.append(str(folder.resolve()))
    folder.rmdir()
    return deleted
    

def list_recursively(folder: Path, file_name = None) -> list:
    res = []
    for d in folder.iterdir():
        if d.is_dir():
            res.extend(list_recursively(d, file_name))

        if file_name:
            if file_name != d.name:
                continue
        res.append(d)
    return res

def delete_pycache(folder: Path = None):
    if folder is None:
        # folder = Path(__file__).parent
        folder = Path.cwd()
    
    for pycache in list_recursively(folder, "__pycache__"):
        print("\n".join(recursive_delete(pycache)))



if __name__ == "__main__":
    delete_pycache()