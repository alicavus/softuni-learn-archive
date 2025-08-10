class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type: str = flour_type
        self.baking_technique: str = baking_technique
        self.weight: float = weight
    
    @property
    def flour_type(self) -> str:
        return self.__flour_type
    
    @property
    def baking_technique(self) -> str:
        return self.__baking_technique
    
    @property
    def weight(self) -> float:
        return self.__weight
    
    @flour_type.setter
    def flour_type(self, value: str):
        if not value:
            raise ValueError("The flour type cannot be an empty string")
        self.__flour_type: str = value
    
    @baking_technique.setter
    def baking_technique(self, value: str):
        if not value:
            raise ValueError("The baking technique cannot be an empty string")
        self.__baking_technique: str = value
    
    @weight.setter
    def weight(self, value: float):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight: float = value