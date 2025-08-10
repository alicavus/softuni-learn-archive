from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    @property
    def _data(self) -> dict:
        return {
            "max mileage": 180.00,
            "additional reduce": 5
        }

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self._data.get("max mileage", 0))
