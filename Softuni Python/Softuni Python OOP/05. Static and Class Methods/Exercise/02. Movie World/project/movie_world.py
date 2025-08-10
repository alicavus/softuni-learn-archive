from project.customer import Customer
from project.dvd import DVD

class MovieWorld:
    DVD_CAPACITY: int = 15
    CUSTOMERS_CAPACITY: int = 10
    
    def __init__(self, name: str):
        self.name: str = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []
    
    @classmethod
    def dvd_capacity(cls) -> int:
        return cls.DVD_CAPACITY
    
    @classmethod
    def customer_capacity(cls) -> int:
        return cls.CUSTOMERS_CAPACITY
    
    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
    
    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def select_customer(self, customer_id) -> Customer | None:
        return next((c for c in self.customers if c.id == customer_id), None)
    
    def select_dvd(self, dvd_id: int) -> DVD | None:
        return next((d for d in self.dvds if d.id == dvd_id), None)
    
    def rent_dvd(self, customer_id: int, dvd_id: int) -> str | None:
        customer = self.select_customer(customer_id)
        dvd = self.select_dvd(dvd_id)

        if not customer or not dvd:
            return

        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            return "DVD is already rented"
        
        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"
    

    def return_dvd(self, customer_id, dvd_id) -> str | None:
        customer = self.select_customer(customer_id)
        dvd = self.select_dvd(dvd_id)

        if not customer or not dvd:
            return
        
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        
        return f"{customer.name} does not have that DVD"
    
    def __repr__(self) -> str:
        res = [customer.__repr__() for customer in self.customers]
        res.extend([dvd.__repr__() for dvd in self.dvds])

        return "\n".join(res)
        



        

    

        