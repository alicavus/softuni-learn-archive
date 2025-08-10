from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__()
        self.fuel_quantity: float = fuel_quantity
        self.fuel_consumption: float = fuel_consumption
    
    @property
    @abstractmethod
    def increased_consumption(self):
        raise NotImplementedError("Inherited class is not inplemented!")

    @abstractmethod
    def drive(self, distance: float):
        raise NotImplementedError("Inherited class is not inplemented!")
    
    @abstractmethod
    def refuel(self, fuel: float):
        raise NotImplementedError("Inherited class is not inplemented!")


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
    
    @property
    def increased_consumption(self):
        return 0.9
    
    def drive(self, distance: float):
        fuel_needed = (self.increased_consumption + self.fuel_consumption) * distance
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed
    
    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
    
    @property
    def increased_consumption(self):
        return 1.6
    
    @property
    def refuel_percentage(self):
        return 0.95
    
    def drive(self, distance: float):
        fuel_needed = (self.increased_consumption + self.fuel_consumption) * distance
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed
    
    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * self.refuel_percentage
    


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
