
class User:
    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.driving_license_number: str = driving_license_number
        self.rating: float = 0
        self.is_blocked: bool = False

    
    @property
    def first_name(self) -> str:
        return self._first_name
    
    @first_name.setter
    def first_name(self, value: str):
        if not value.strip():
            raise ValueError("First name cannot be empty!")
        self._first_name: str = value
    
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @last_name.setter
    def last_name(self, value: str):
        if not value.strip():
            raise ValueError("Last name cannot be empty!")
        self._last_name: str = value
    
    @property
    def driving_license_number(self) -> str:
        return self._driving_license_number
    
    @driving_license_number.setter
    def driving_license_number(self, value: str):
        if not value.strip():
            raise ValueError("Driving license number is required!")
        self._driving_license_number: str = value
    
    @property
    def rating(self) -> float:
        return self._rating
    
    @rating.setter
    def rating(self, value: float):
        if value < 0.0:
            raise ValueError("Users rating cannot be negative!")
        self._rating: float = value
    
    def increase_rating(self):
        INCREASE_BY = 0.5
        RATING_MAX_VALUE = 10
        new_rating = self.rating + INCREASE_BY
        self.rating = RATING_MAX_VALUE if new_rating > RATING_MAX_VALUE else new_rating
    
    def decrease_rating(self):
        DECREASE_BY = 2.0
        RATING_MIN_VALUE = 0
        new_rating = self.rating - DECREASE_BY
        if new_rating < RATING_MIN_VALUE:
            self.is_blocked = True
            new_rating = RATING_MIN_VALUE
        self.rating = new_rating
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} Driving license: {self.driving_license_number} Rating: {self.rating}"



