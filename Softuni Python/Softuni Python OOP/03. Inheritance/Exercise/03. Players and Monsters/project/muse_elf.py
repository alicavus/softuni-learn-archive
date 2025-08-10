from project.elf import Elf

class MuseElf(Elf):
    def __init__(self, username: str, level: str):
        super().__init__(username, level)