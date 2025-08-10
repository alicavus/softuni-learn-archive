from project.product import Product

FOOD_QUANTITY = 15

class Food(Product):
    def __init__(self, name: str):
        super().__init__(name, quantity=FOOD_QUANTITY)