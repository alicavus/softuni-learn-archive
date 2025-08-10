from abc import ABC, abstractmethod
from project.food import Food

class Animal(ABC):
    def __init__(self, name: str, weight: float):
        super().__init__()
        self.name: str = name
        self.weight: float = weight
        self.food_eaten: int = 0
    
    @abstractmethod
    def make_sound(self):
        raise NotImplementedError("Subclass must implement")
    
    @abstractmethod
    def feed(self, food: Food):
        raise NotImplementedError("Subclass must implement")

class Bird(Animal):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size: float = wing_size
    
    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Mammal(Animal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region: str = living_region
    
    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


