from project.album import Album

class Band:
    def __init__(self, name: str):
        self.name: str = name
        self.albums: list[Album] = []
    
    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums += [album]
        return f"Band {self.name} has added their newest album {album.name}."
    
    def remove_album(self, album_name: str) -> str:
        for idx, album in enumerate(self.albums):
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                self.albums.pop(idx)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."
    
    def details(self) -> str:
        result: list[str] = [f"Band {self.name}"]
        result.extend([album.details() for album in self.albums])
        return "\n".join(result)