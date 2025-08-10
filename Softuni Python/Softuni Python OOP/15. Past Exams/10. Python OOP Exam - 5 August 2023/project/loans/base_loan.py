from abc import ABC, abstractmethod

class BaseLoan(ABC):
    def __init__(self, interest_rate: float, amount: float):
        self.amount: float = amount
        self.interest_rate: float = interest_rate

    def increase_interest_rate(self):
        self.interest_rate += self._data.get("increase interest", 0)

    @property
    @abstractmethod
    def _data(self) -> dict:
        pass