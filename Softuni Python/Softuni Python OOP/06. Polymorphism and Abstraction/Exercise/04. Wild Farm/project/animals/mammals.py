from abc import ABC, abstractmethod
from project.animals.animal import Animal, Mammal
from project.food import Food, Fruit, Vegetable, Meat, Seed

class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
    
    def make_sound(self):
        return "Squeak"
    
    def feed(self, food):
        if type(food) not in [Vegetable, Fruit]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.1 * food.quantity
        self.food_eaten += 1 * food.quantity

class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
    
    def make_sound(self):
        return "Woof!"
    
    def feed(self, food):
        if type(food) not in [Meat]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.4 * food.quantity
        self.food_eaten += 1 * food.quantity

class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
    
    def make_sound(self):
        return "Meow"
    
    def feed(self, food):
        if type(food) not in [Vegetable, Meat]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.3 * food.quantity
        self.food_eaten += 1 * food.quantity

class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
    
    def make_sound(self):
        return "ROAR!!!"
    
    def feed(self, food):
        if type(food) not in [Meat]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 1 * food.quantity
        self.food_eaten += 1 * food.quantity