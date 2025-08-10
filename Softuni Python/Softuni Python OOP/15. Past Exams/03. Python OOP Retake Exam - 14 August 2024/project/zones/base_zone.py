from abc import ABC, abstractmethod
from project.battleships.base_battleship import BaseBattleship

class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code: str = code
        self.volume: int = volume
        self.ships: list[BaseBattleship] = []

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value: str):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code: str = value

    def get_ships(self):
        return sorted(self.ships, key=lambda ship: (-ship.hit_strength, ship.name))

    def zone_info(self):
        data = {
            "Royal Zone": "Pirate Battleship",
            "Pirate Zone": "Royal Battleship"
        }
        result = [f"@{str(self)} Statistics@", f"Code: {self.code}; Volume: {self.volume}"]
        enemy_str = data[str(self)]
        enemies_count = ["e" for enemy in self.ships if str(enemy) == enemy_str]

        result.append(
            f"Battleships currently in the {str(self)}: {len(self.ships)}, {len(enemies_count)} out of them are {enemy_str}s."
        )

        if self.ships:
            ships_names = ", ".join([ship.name for ship in self.get_ships()])
            result.append(f"#{ships_names}#")

        return  "\n".join(result)

    @abstractmethod
    def __str__(self):
        pass