from project.beverage.hot_beverage import HotBeverage

class Coffee(HotBeverage):
    MILLILITERS: float = 50
    PRICE: float = 3.50
    def __init__(self, name: str, caffeine: float):
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.__caffeine: float = caffeine
    
    @property
    def caffeine(self) -> float:
        return self.__caffeine