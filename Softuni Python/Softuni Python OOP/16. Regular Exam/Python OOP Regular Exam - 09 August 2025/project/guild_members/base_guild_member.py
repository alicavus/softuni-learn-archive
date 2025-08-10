from abc import ABC, abstractmethod

class BaseGuildMember(ABC):
    def __init__(self, tag: str, gold: int, role: str, skill_level: int):
        self.tag: str = tag
        self.gold: int = gold
        self.role: str = role
        self.skill_level: int = skill_level
    
    @property
    def tag(self) -> str:
        return self._tag
    
    @tag.setter
    def tag(self, value: str):
        if not value.isalnum():
            raise ValueError("Tag must contain only letters and digits!")
        self._tag: str = value
    
    @property
    def gold(self) -> int:
        return self._gold
    
    @gold.setter
    def gold(self, value: int):
        if value < 0:
            raise ValueError("Gold must be a non-negative integer!")
        self._gold: int = value
    
    @property
    def role(self) -> str:
        return self._role
    
    @role.setter
    def role(self, value: str):
        if not value.strip():
            raise ValueError("Role cannot be empty!")
        self._role: str = value
    
    @property
    def skill_level(self) -> int:
        return self._skill_level
    
    @skill_level.setter
    def skill_level(self, value: int):
        if not 1 <= value <= 10:
            raise ValueError("Skill level is out of range!")
        self._skill_level: int = value
    
    @property
    @abstractmethod
    def _data(self) -> dict:
        pass
    
    @abstractmethod
    def practice(self):
        pass
