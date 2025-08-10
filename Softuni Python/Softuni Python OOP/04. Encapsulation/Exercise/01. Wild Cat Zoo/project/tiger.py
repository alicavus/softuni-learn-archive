from project.animal import Animal

TIGER_MONEY_FOR_CARE = 45

class Tiger(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, TIGER_MONEY_FOR_CARE)