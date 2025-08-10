from abc import ABC, abstractmethod

class BaseClimber(ABC):
    def __init__(self, name: str, strength: float):
        self.name: str = name
        self.strength: float = strength
        self.conquered_peaks: list = []
        self.is_prepared: bool = True
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")
        self._name: str = value
    
    @property
    def strength(self) -> float:
        return self._strength
    
    @strength.setter
    def strength(self, value: float):
        if value <= 0.0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self._strength: float = value
    
    @property
    @abstractmethod
    def _data(self) -> dict:
        pass
    
    def can_climb(self):
        return self._data.get("required climbing strength", 0) <= self.strength

    def climb(self, peak):
        multiplied_data = self._data.get("multiplied by", (0, 0, None))
        self.strength -= self._data.get("reduced by", 0) * multiplied_data[1 if peak.difficulty_level == multiplied_data[2] else 0]
        peak.is_conquered = True
        self.conquered_peaks.append(peak.name)

    def rest(self):
        INCREASE_STRENGTH_VALUE = 15
        self.strength += INCREASE_STRENGTH_VALUE
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered peaks: {', '.join(sorted(peak for peak in self.conquered_peaks))} ///"
    
