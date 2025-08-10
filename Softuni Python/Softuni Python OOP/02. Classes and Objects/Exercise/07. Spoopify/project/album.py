from project.song import Song

class Album:
    def __init__(self, name: str, *songs: Song):
        self.name: str = name
        self.songs: list[Song] = [song for song in songs]
        self.published = False
    
    def add_song(self, song: Song) -> str:
        if self.published:
            return "Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        elif song in self.songs:
            return "Song is already in the album."
        self.songs += [song]
        return f"Song {song.name} has been added to the album {self.name}." 
    
    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."
        for idx, song in enumerate(self.songs):
            if song.name == song_name:
                self.songs.pop(idx)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."
    
    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."
    
    def details(self) -> str:
        result: list[str] = [f"Album {self.name}"]
        result.extend([f" == {song.get_info()}" for song in self.songs])

        return "\n".join(result)
