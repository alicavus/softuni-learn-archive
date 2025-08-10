from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.route import Route
from project.user import User

class ManagingApp:
    VEHICLE_TYPES = {
        "CargoVan": CargoVan,
        "PassengerCar": PassengerCar
    }
    def __init__(self):
        self.routes: list[Route] = []
        self.users: list[User] = []
        self.vehicles: list[BaseVehicle] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self.get_item(self.users, "driving_license_number", driving_license_number)
        if user is not None:
            return f"{driving_license_number} has already been registered to our platform."
        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        cls = self.VEHICLE_TYPES.get(vehicle_type)
        vehicle = self.get_item(self.vehicles, "license_plate_number", license_plate_number)
        if cls is None:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if vehicle is not None:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(cls(brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route: Route = self.get_item(self.routes, {"start_point": start_point, "end_point": end_point, "length": length})
        if route is not None:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."
        route: Route = self.get_item(self.routes, {"start_point": start_point, "end_point": end_point})
        if route is not None:
            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif route.length > length:
                route.is_locked = True
        self.routes.append(Route(start_point, end_point, length, len(self.routes)+1))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user: User = self.get_item(self.users, "driving_license_number", driving_license_number)
        vehicle: BaseVehicle = self.get_item(self.vehicles, "license_plate_number", license_plate_number)
        route: Route = self.get_item(self.routes, "route_id", route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()

        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = sorted(self.get_items(self.vehicles, "is_damaged", True), key=lambda v: (v.brand, v.model))[:count]

        cnt = 0
        for vehicle in damaged_vehicles:
            vehicle.change_status()
            vehicle.recharge()
            cnt += 1
        return f"{cnt} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        users = sorted(self.users, key=lambda u: -u.rating)
        result.extend(str(user) for user in users)

        return "\n".join(result)


    @staticmethod
    def get_item(collection, attribute_name = None, attribute_value = None):
        if attribute_name is None:
            return next((item for item in collection), None)
        if isinstance(attribute_name, dict):
            return next((item for item in collection if all(getattr(item, k, None) == v for k, v in attribute_name.items())), None)
        return next((item for item in collection if getattr(item, attribute_name, None) == attribute_value), None)

    @staticmethod
    def get_items(collection, attribute_name = None, attribute_value = None):
        if attribute_name is None:
            return (item for item in collection)
        return (item for item in collection if getattr(item, attribute_name, None) == attribute_value)
