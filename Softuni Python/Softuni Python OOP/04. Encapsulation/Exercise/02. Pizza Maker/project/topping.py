class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type: str = topping_type
        self.weight: float = weight
    
    @property
    def topping_type(self) -> str:
        return self.__topping_type
    
    @property
    def weight(self) -> float:
        return self.__weight
    
    @topping_type.setter
    def topping_type(self, value: str):
        if not value:
            raise ValueError("The topping type cannot be an empty string")
        self.__topping_type: str = value
    
    @weight.setter
    def weight(self, value: float):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight: float = value
    

    
