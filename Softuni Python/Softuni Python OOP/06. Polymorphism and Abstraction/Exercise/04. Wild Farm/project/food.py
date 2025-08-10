from abc import ABC, abstractmethod

class Food(ABC):
    def __init__(self, quantity: int):
        if type(self) is Food:
            raise NotImplementedError("Base class is abstract")
        self.quantity: int = quantity
        super().__init__()

class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)
    

class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity)

class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)

class Seed(Food):
    def __init__(self, quantity):
        super().__init__(quantity)
