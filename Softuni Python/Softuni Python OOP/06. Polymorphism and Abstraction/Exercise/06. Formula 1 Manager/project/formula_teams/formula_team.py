from abc import ABC, abstractmethod

class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget: int = budget
        self.sponsors: dict[str, dict[int, int]] = None
        self.expences: int = None
    
    @property
    def budget(self):
        return self.__budget
    
    @budget.setter
    def budget(self, value: int):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value
    
    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for sponsor in self.sponsors:
            for pos, prize in sorted(self.sponsors[sponsor].items()):
                if race_pos <= pos:
                    revenue += prize
                    break
        
        revenue -= self.expences

        self.budget += revenue
        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"

