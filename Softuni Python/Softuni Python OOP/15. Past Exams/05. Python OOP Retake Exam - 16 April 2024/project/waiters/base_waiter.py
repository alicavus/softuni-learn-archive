from abc import ABC, abstractmethod

class BaseWaiter(ABC):
    def __init__(self, name: str, hours_worked: int):
        self.name: str = name
        self.hours_worked: int = hours_worked
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        MIN_LEN, MAX_LEN = 3, 50
        if not MIN_LEN <= len(value) <= MAX_LEN:
            raise ValueError(f"Waiter name must be between {MIN_LEN} and {MAX_LEN} characters in length!")
        self.__name: str = value
    
    @property
    def hours_worked(self) -> int:
        return self.__hours_worked
    
    @hours_worked.setter
    def hours_worked(self, value: int):
        if value < 0:
            raise ValueError("Cannot have negative hours worked!")
        self.__hours_worked: int = value

    @property
    @abstractmethod
    def _data(self):
        pass

    def calculate_earnings(self):
        return self.hours_worked * self._data['hourly wage']

    def report_shift(self):
        return  f"{self.name} worked a {self._data['shift type']} shift of {self.hours_worked} hours."

    def __str__(self):
        return f"Name: {self.name}, Total earnings: ${self.calculate_earnings():.2f}"