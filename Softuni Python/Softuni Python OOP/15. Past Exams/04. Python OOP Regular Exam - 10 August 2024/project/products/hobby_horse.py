from project.products.base_product import BaseProduct

class HobbyHorse(BaseProduct):
    @property
    def _data(self):
        return {
            "material": "Wood/Plastic",
            "sub type": "Toys",
            "discount": 0.2
        }
    
    def __init__(self, model: str, price: float):
        super().__init__(model, price, self._data["material"], self._data["sub type"])
    
    def __str__(self):
        return "HobbyHorse"