from project.dough import Dough
from project.topping import Topping

class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name: str = name
        self.dough: Dough = dough
        self.max_number_of_toppings: int = max_number_of_toppings
        self.toppings: dict[str, float] = {}
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def dough(self) -> Dough:
        return self.__dough
    
    @property
    def max_number_of_toppings(self) -> int:
        return self.__max_number_of_toppings
    
    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name: str = value
    
    @dough.setter
    def dough(self, value: Dough):
        if not value:
            raise ValueError("You should add dough to the pizza")
        self.__dough: Dough = value
    
    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value: int):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings: int = value
    

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        if not topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type] += topping.weight
    
    def calculate_total_weight(self) -> float:
        toppings_weight = sum(topping for topping in self.toppings.values()) if self.toppings else 0
        doghs_weight = self.dough.weight

        return toppings_weight + doghs_weight
    
    