from abc import ABC, abstractmethod

class BaseEquipment(ABC):
    def __init__(self, protection: int, price: float):
        self.protection: int = protection
        self.price: float = price
    
    def increase_price(self):
        self.price *= 1 + self._data.get("increase rate", 0)

    @property
    @abstractmethod
    def _data(self) -> dict:
        pass