from abc import ABC, abstractmethod

class BaseBattleship(ABC):
    def __init__(self, name: str, health: int, hit_strength: int, ammunition: int):
        self.name: str = name
        self.health: int = health
        self.hit_strength: int = hit_strength
        self.ammunition: int = ammunition
        self.is_attacking: bool = False
        self.is_available: bool = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalpha():
            raise ValueError("Ship name must contain only letters!")
        self.__name: str = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value: int):
        self.__health = max(0, value)

    def take_damage(self, enemy_battleship: "BaseBattleship"):
        self.health -= enemy_battleship.hit_strength

    @abstractmethod
    def __str__(self):
        pass

    def attack(self):
        self.ammunition = max(self.ammunition - self.REDUCE_AMMUNITION, 0)



