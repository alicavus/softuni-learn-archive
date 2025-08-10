from abc import ABC, abstractmethod

class BasePeak(ABC):
    def __init__(self, name: str, elevation: int):
        self.name: str = name
        self.elevation: int = elevation
        self.difficulty_level: str = self.calculate_difficulty_level()
        self.is_conquered: bool = False
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        SYMBOLS_MIN_LEN = 2
        if len(value) < SYMBOLS_MIN_LEN:
            raise ValueError(f"Peak name cannot be less than {SYMBOLS_MIN_LEN} symbols!")
        self._name: str = value
    
    @property
    def elevation(self) -> int:
        return self._elevation
    
    @elevation.setter
    def elevation(self, value: int):
        ELEVATIN_MIN_VALUE = 1_500
        if value < ELEVATIN_MIN_VALUE:
            raise ValueError(f"Peak elevation cannot be below {ELEVATIN_MIN_VALUE}m.")
        self._elevation: int = value
    
    @property
    @abstractmethod
    def _data(self) -> dict:
        pass
    
    def get_recommended_gear(self):
        return self._data.get("recommended gear", [])

    def calculate_difficulty_level(self):
        data = self._data.get("difficulty level", (0, 0))
        return "Extreme" if self.elevation > data[1] else "Advanced" if data[0] <= self.elevation <= data[1] else None