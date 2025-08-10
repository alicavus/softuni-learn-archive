from abc import ABC, abstractmethod

class BaseArtifact(ABC):
    def __init__(self, name: str, price: float, space_required: int):
        self.name: str = name
        self.price: float = price
        self.space_required: int = space_required
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Artifact name cannot be null or empty!")
        self._name = value
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError("Artifact price should be more than 0.0!")
        self._price = value
    
    @property
    def space_required(self) -> int:
        return self._space_required
    
    @space_required.setter
    def space_required(self, value):
        if value < 1 or value > 1_000:
            raise ValueError("Space required for the artifact exhibition must be between 1 and 1000!")
        self._space_required = value
    
    @property
    @abstractmethod
    def _artifact_type(self) -> str:
        pass

    def artifact_information(self) -> str:
        return f"{self._artifact_type}: {self.name}; Price: {self.price:.2f}; Required space: {self.space_required}"