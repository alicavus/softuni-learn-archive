from abc import ABC, abstractmethod

class Musician(ABC):
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
        self.skills: list = []
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Musician name cannot be empty!")
        self._name: str = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if value < self._data.get("legal age", 16):
            raise ValueError(f"Musicians should be at least {self._data.get('legal age', 16)} years old!")
        self._age: int = value

    @property
    @abstractmethod
    def _data(self) -> dict:
        pass

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self._data.get("skills set", []):
            raise ValueError(f"{new_skill} is not a needed skill!")
        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."

    def is_skilled(self, skills: list):
        return all(skill in self.skills for skill in skills)
