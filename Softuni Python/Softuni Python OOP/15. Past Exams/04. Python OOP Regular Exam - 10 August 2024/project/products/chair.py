from project.products.base_product import BaseProduct

class Chair(BaseProduct):
    @property
    def _data(self):
        return {
            "material": "Wood",
            "sub type": "Furniture",
            "discount": 0.1
        }
    
    def __init__(self, model: str, price: float):
        super().__init__(model, price, self._data["material"], self._data["sub type"])
    
    def __str__(self):
        return "Chair"
    

    