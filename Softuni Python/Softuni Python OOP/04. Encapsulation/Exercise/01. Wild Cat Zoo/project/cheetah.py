from project.animal import Animal

CHEETAH_MONEY_FOR_CARE = 60

class Cheetah(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, CHEETAH_MONEY_FOR_CARE)