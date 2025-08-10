from abc import ABC, abstractmethod
from project.animals.animal import Animal, Bird
from project.food import Food, Fruit, Vegetable, Meat, Seed

class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
    
    def make_sound(self):
        return "Hoot Hoot"
    
    def feed(self, food):
        if type(food) not in [Meat]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.25 * food.quantity
        self.food_eaten += 1 * food.quantity

class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
    
    def make_sound(self):
        return "Cluck"
    
    def feed(self, food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += 1 * food.quantity
        