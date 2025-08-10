from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__()
        self.name: str = name
        self.age: int = age
        self.gender: str = gender
    
    def __repr__(self):
         return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
 

    @abstractmethod
    def make_sound(self):
        raise NotImplementedError("Subclass must implement")
