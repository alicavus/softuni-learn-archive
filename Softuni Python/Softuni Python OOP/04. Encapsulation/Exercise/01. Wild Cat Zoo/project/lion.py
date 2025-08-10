from project.animal import Animal

LION_MONEY_FOR_CARE = 50

class Lion(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, LION_MONEY_FOR_CARE)