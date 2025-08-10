from abc import ABC, abstractmethod

class BaseFish(ABC):
    def __init__(self, name: str, points: float, time_to_catch: int):
        self.name: str = name
        self.points: float = points
        self.time_to_catch: int = time_to_catch

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Fish name should be determined!")
        self._name: str = value

    @property
    def points(self) -> float:
        return self._points

    @points.setter
    def points(self, value: float):
        POINTS_MIN_VALUE = 1
        POINTS_MAX_VALUE = 10
        if not POINTS_MIN_VALUE <= value <= POINTS_MAX_VALUE:
            raise ValueError(f"Points should be a value ranging from {POINTS_MIN_VALUE} to {POINTS_MAX_VALUE}!")
        self._points: float = value

    @property
    @abstractmethod
    def TIME_TO_CATCH(self):
        pass

    def fish_details(self):
        return f"{self.__class__.__name__}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"