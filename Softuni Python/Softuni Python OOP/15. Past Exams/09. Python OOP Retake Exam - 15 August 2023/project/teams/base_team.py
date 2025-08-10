from abc import ABC, abstractmethod

class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name: str = name
        self.country: str = country
        self.advantage: int = advantage
        self.budget: float = budget
        self.wins: int = 0
        self.equipment: list = []
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Team name cannot be empty!")
        self._name: str = value
    
    @property
    def country(self) -> str:
        return self._country
    
    @country.setter
    def country(self, value: str):
        COUNTRY_MIN_LEN = 2
        if len(value.strip()) < COUNTRY_MIN_LEN:
            raise ValueError(f"Team country should be at least {COUNTRY_MIN_LEN} symbols long!")
        self._country: str = value
    
    @property
    def advantage(self) -> int:
        return self._advantage

    @advantage.setter
    def advantage(self, value: int):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self._advantage: int = value
    
    @property
    def equipement_stats(self) -> dict:
        price = 0
        protection = 0
        cnt = 0
        for equipement in self.equipment:
            price += equipement.price
            protection += equipement.protection
            cnt += 1
        return {
            "price": price,
            "protection": protection,
            "count": cnt
        }
    
    @property
    @abstractmethod
    def _data(self) -> dict:
        pass
    
    def win(self):
        self.wins += 1
        self.advantage += self._data.get("increase advantage", 0)
    
    def get_statistics(self):
        total_price, total_protection, count = self.equipement_stats.values()
        result = [
            f"Name: {self.name}",
            f"Country: {self.country}",
            f"Advantage: {self.advantage} points",
            f"Budget: {self.budget:.2f}EUR",
            f"Wins: {self.wins}",
            f"Total Equipment Price: {total_price:.2f}",
            f"Average Protection: {int(total_protection/count) if count else 0}"
        ]

        return "\n".join(result)


