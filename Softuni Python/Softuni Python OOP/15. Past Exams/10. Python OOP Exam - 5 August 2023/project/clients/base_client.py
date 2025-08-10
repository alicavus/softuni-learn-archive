from abc import ABC, abstractmethod

class BaseClient(ABC):
    def __init__(self, name: str, client_id: str, income: float, interest: float):
        self.name: str = name
        self.client_id: str = client_id
        self.income: float = income
        self.interest: float = interest
        self.loans = []
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value.split():
            raise ValueError("Client name cannot be empty!")
        self._name: str = value
    
    @property
    def client_id(self) -> str:
        return self._client_id
    
    @client_id.setter
    def client_id(self, value: str):
        CLIENT_ID_LEN = 10
        if len(value) != CLIENT_ID_LEN:
            raise ValueError(f"Client ID should be {CLIENT_ID_LEN} symbols long!")
        self._client_id: str = value
    
    @property
    def income(self) -> float:
        return self._income
    
    @income.setter
    def income(self, value: float):
        if value <= 0.0:
            raise ValueError("Income must be greater than zero!")
        self._income: float = value

    @property
    @abstractmethod
    def _data(self) -> dict:
        pass

    def increase_clients_interest(self):
        self.interest += self._data.get("increase interest", 0)

