from abc import ABC, abstractmethod

class BaseVehicle(ABC):
    MAX_BATTERY_LEVEL = 100
    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand: str = brand
        self.model: str = model
        self.license_plate_number: str = license_plate_number
        self.max_mileage: float = max_mileage
        self.battery_level: int = self.__class__.MAX_BATTERY_LEVEL
        self.is_damaged: bool = False
    
    @property
    def brand(self) -> str:
        return self._brand
    
    @brand.setter
    def brand(self, value: str):
        if not value.strip():
            raise ValueError("Brand cannot be empty!")
        self._brand: str = value
    
    @property
    def model(self) -> str:
        return self._model
    
    @model.setter
    def model(self, value: str):
        if not value.strip():
            raise ValueError("Model cannot be empty!")
        self._model: str = value
    
    @property
    def license_plate_number(self) -> str:
        return self._license_plate_number
    
    @license_plate_number.setter
    def license_plate_number(self, value: str):
        if not value.strip():
            raise ValueError("License plate number is required!")
        self._license_plate_number: str = value

    @property
    @abstractmethod
    def _data(self) -> dict:
        pass
    
    def drive(self, mileage: float):
        self.battery_level -= round(mileage / self.max_mileage * 100 + self._data.get("additional reduce", 0))

    def recharge(self):
        self.battery_level = self.__class__.MAX_BATTERY_LEVEL

    def change_status(self):
        self.is_damaged = not self.is_damaged

    def __str__(self):
        return f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% Status: {'Damaged' if self.is_damaged else 'OK'}"
