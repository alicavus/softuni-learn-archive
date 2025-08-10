from abc import ABC, abstractmethod

class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.name: str = name
        self.capacity: int = capacity
        self.robots: list = []
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Service name cannot be empty!")
        self._name: str = value
    
    @property
    def capacity(self) -> float:
        return self._capacity
    
    @capacity.setter
    def capacity(self, value: float):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self._capacity: float = value
    
    @property
    @abstractmethod
    def _data(self) -> dict:
        pass
    
    def details(self) -> str:
        return "\n".join([
            f"{self.name} {self._data.get('service type', '')}:",
            f"Robots: {'none' if not self.robots else ' '.join(robot.name for robot in self.robots)}"
        ])

    
