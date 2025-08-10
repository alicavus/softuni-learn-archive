from abc import ABC, abstractmethod

class BaseProduct(ABC):
    def __init__(self, model: str, price: float, material: str, sub_type: str):
        self.model: str = model
        self.price: float = price
        self.material: str = material
        self.sub_type: str = sub_type
    
    @property
    def model(self) -> str:
        return self.__model
    
    @model.setter
    def model(self, value: str):
        if len(value) < 3 or value.isspace():
            raise ValueError("Product model must be at least 3 chars long!")
        self.__model: str = value
    
    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, value: float):
        if value <= 0.0:
            raise ValueError("Product price must be greater than zero!")
        self.__price: float = value
    
    @property
    @abstractmethod
    def _data(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
    
    def discount(self):
        self.price *= 1 - self._data["discount"]