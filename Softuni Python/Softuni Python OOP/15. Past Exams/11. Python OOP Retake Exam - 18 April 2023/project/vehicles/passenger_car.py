from project.vehicles.base_vehicle import BaseVehicle

class PassengerCar(BaseVehicle):
    @property
    def _data(self) -> dict:
        return {
            "max mileage": 450.00,
            "additional reduce": 0
        }
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self._data.get("max mileage", 0))
