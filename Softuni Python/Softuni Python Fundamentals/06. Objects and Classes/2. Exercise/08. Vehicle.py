class Vehicle:
    def __init__(self, type: str, model: str, price: float):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None
    
    def __repr__(self):
        if self.owner is None:
            return f"{self.model} {self.type} is on sale: {self.price}"
        return f"{self.model} {self.type} is owned by: {self.owner}"
    
    def buy(self, money: int, owner: str):
        if self.owner is None:
            if money >= self.price:
                self.owner = owner
                return f"Successfully bought a {self.type}. Change: {money-self.price:.2f}"
            return "Sorry, not enough money"
        return "Car already sold"
        
    
    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        self.owner = None
    
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
