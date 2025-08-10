from abc import ABC, abstractmethod

class BaseDiver(ABC):
    def __init__(self, name: str, oxygen_level: float):
        self.name: str = name
        self.oxygen_level: float = oxygen_level
        self.catch: list = []
        self.competition_points: float = 0.0
        self.has_health_issue: bool = False
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Diver name cannot be null or empty!")
        self._name: str = value

    @property
    def oxygen_level(self) -> float:
        return self._oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value: float):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self._oxygen_level: float = value

    @property
    def competition_points(self):
        return self._competition_points

    @competition_points.setter
    def competition_points(self, value: float):
        self._competition_points: float = float(f'{value:.1f}')

    @property
    @abstractmethod
    def _data(self):
        pass

    def miss(self, time_to_catch: int):
        new_value = round(self.oxygen_level - self._data.get("miss percent", 0) * time_to_catch)
        self.oxygen_level = new_value if new_value > 0 else 0

    def renew_oxy(self):
        self.oxygen_level = self._data.get("default oxygen level", 0)

    def hit(self, fish):
        oxygen_level = self.oxygen_level - fish.time_to_catch
        self.oxygen_level = oxygen_level if oxygen_level > 0 else 0
        if oxygen_level >= 0:
            self.catch.append(fish)
            self.competition_points += fish.points

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"
