from abc import ABC, abstractmethod
from project.products.base_product import BaseProduct

class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int):
        self.name: str = name
        self.location: str = location
        self.capacity: int = capacity
        self.products: list[BaseProduct] = []
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if not value or value.isspace():
            raise ValueError("Store name cannot be empty!")
        self.__name: str = value
    
    @property
    def location(self) -> str:
        return self.__location
    
    @location.setter
    def location(self, value: str):
        if len(value) != 3 or any([c.isspace() for c in value]):
            raise ValueError("Store location must be 3 chars long!")
        self.__location: str = value
    
    @property
    def capacity(self) -> int:
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value: int):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity: int = value
    
    def get_estimated_profit(self):
        PROFIT_PERCENTAGE = 0.1
        profit = sum(product.price for product in self.products) * PROFIT_PERCENTAGE

        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"
    
    @property
    @abstractmethod
    def store_type(self):
        pass
    
    def store_stats(self):
        products = {}
        for product in self.products:
            if product.model not in products:
                products[product.model] = {
                    "count": 0,
                    "price": 0.0
                }
            products[product.model]["count"] += 1
            products[product.model]["price"] += product.price
        
        sorted_products = sorted(products.items(), key=lambda item: item)
            
        result = [
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
            self.get_estimated_profit(),
            f"**{str(self)} for sale:"
        ]

        result.extend([f"{model}: {data['count']}pcs, average price: {data['price']/data['count']:.2f}" for model, data in sorted_products])

        return "\n".join(result)

    @abstractmethod
    def __str__(self):
        pass

    @staticmethod
    def get_item(collection, attribute_name, attribute_value):
        return next((item for item in collection if getattr(item, attribute_name) == attribute_value), None)
    
    @staticmethod
    def get_items(collection, attribute_name = None, attribute_value = None):
        if not attribute_name and not attribute_value:
            return (item for item in collection)
        return (item for item in collection if getattr(item, attribute_name) == attribute_value)
