from abc import ABC, abstractmethod

class BaseGuildHall(ABC):
    def __init__(self, alias: str):
        self.alias: str = alias
        self.members: list = []
    
    @property
    def alias(self) -> str:
        return self._alias
    
    @alias.setter
    def alias(self, value: str):
        _v = value.strip()
        if len(_v) < 2 or any(not (c.isalpha() or c.isspace()) for c in _v):
            raise ValueError("Guild hall alias is invalid!")
        self._alias: str = value
    
    @property
    def max_member_count(self) -> int:
        return self._data.get("max member count", 0)
    
    @property
    @abstractmethod
    def _data(self) -> dict:
        pass

    def calculate_total_gold(self):
        return sum(member.gold for member in self.members)

    def calculate_total_skill_level(self):
        return sum(member.skill_level for member in self.members)
    
    def status(self):
        members = [member.tag for member in self.members]
        return f"Guild hall: {self.alias}; Members: {' *'.join(sorted(members)) if members else 'N/A'}; Total gold: {self.calculate_total_gold()}"
    
    @abstractmethod
    def increase_gold(self, min_skill_level_value: int):
        pass
    