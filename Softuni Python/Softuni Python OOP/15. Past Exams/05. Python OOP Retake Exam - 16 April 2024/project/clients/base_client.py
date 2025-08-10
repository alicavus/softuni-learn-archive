from abc import ABC, abstractmethod

class BaseClient(ABC):
    def __init__(self, name: str, membership_type: str):
        self.name : str = name
        self.membership_type: str = membership_type
        self.points: int = 0

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Client name should be determined!")
        self.__name: str = value
    
    @property
    def membership_type(self) -> str:
        return self.__membership_type


    @membership_type.setter
    def membership_type(self, value: str):
        VALID_MEMBERSHIP_TYPES = ["Regular", "VIP"]
        if value not in VALID_MEMBERSHIP_TYPES:
            raise ValueError(f"Invalid membership type. Allowed types: {', '.join(VALID_MEMBERSHIP_TYPES)}.")
        self.__membership_type: str = value

    @property
    @abstractmethod
    def _points_multiplier(self):
        pass

    def earning_points(self, order_amount: float) -> int:
        earned = int(order_amount * self._points_multiplier)
        self.points += earned
        return earned

    def apply_discount(self):
        DISCOUNTS = {
            100: 10,
            50: 5,
            0: 0
        }
        for points in DISCOUNTS:
            if self.points >= points:
                discount_percentage = DISCOUNTS[points]
                self.points -= points
                return discount_percentage, self.points