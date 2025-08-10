from project.product import Product

DRINK_QUANTITY = 10

class Drink(Product):
    def __init__(self, name: str):
        super().__init__(name, quantity=DRINK_QUANTITY)