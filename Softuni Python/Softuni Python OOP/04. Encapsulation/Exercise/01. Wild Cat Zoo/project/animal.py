class Animal:
    '''Base class for Zoo animals'''
    def __init__(self, name: str, gender: str, age: int, money_for_care: int):
        self.name: str = name
        self.gender: str = gender
        self.age: int = age
        self.money_for_care: int = money_for_care
    
    def __repr__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"