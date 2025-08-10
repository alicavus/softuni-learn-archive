from abc import ABC, abstractmethod
from project.artifacts import BaseArtifact

class BaseCollector(ABC):
    def __init__(self, name: str, available_money: float, available_space: int):
        self.name: str = name
        self.available_money: float = available_money
        self.available_space: int = available_space
        self.purchased_artifacts: list[BaseArtifact] = []
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        value = value.strip()
        if not value or not self.validate_name(value):
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self._name: str = value
    
    @property
    def available_money(self) -> float:
        return self._available_money
    
    @available_money.setter
    def available_money(self, value: float):
        if value < 0.0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self._available_money: float = value
    
    @property
    def available_space(self) -> int:
        return self._available_space
    
    @available_space.setter
    def available_space(self, value: int):
        if value <= 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self._available_space: int = value
    
    @property
    @abstractmethod
    def DATA(self) -> dict:
        pass
    
    def increase_money(self):
        self.available_money += self.DATA["increase money"]

    def can_purchase(self, artifact_price: float, artifact_space_required: int) -> bool:
        return self.available_money >= artifact_price and self.available_space >= artifact_space_required
    
    def __str__(self) -> str:
        artifacts = ", ".join([artifact.name for artifact in sorted(self.purchased_artifacts, key=lambda item: item.name, reverse=True)]) if self.purchased_artifacts else "none"
        return f"Collector name: {self.name}; Money available: {self.available_money:.2f}; Space available: {self.available_space}; Artifacts: {artifacts}"

    # helper functions
    @staticmethod
    def validate_name(value: str):
        if not value or value.isspace():
            return False
        return all([c.isalnum() or c.isspace() for c in value])
