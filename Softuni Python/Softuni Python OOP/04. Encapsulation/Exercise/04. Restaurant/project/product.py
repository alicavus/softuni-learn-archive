class Product:
    def __init__(self, name: str, price: float):
        self.__name: str = name
        self.__price: float = price
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def price(self) -> float:
        return self.__price