from abc import ABC, abstractmethod

class BaseRobot(ABC):
    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name: str = name
        self.kind: str = kind
        self.price: float = price
        self.weight: int = weight
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Robot name cannot be empty!")
        self._name: str = value
    
    @property
    def kind(self) -> str:
        return self._kind
    
    @kind.setter
    def kind(self, value: str):
        if not value.strip():
            raise ValueError("Robot kind cannot be empty!")
        self._kind: str = value
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float):
        if value <= 0.0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")
        self._price: float = value
    
    def eating(self):
        self.weight += self._data.get("increase weight", 0)

    @property
    @abstractmethod
    def _data(self) -> dict:
        pass