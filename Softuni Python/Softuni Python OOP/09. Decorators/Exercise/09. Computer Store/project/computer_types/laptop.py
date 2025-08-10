from project.computer_types.computer import Computer

class Laptop(Computer):
    @property
    def CPU(self):
        return {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200        
        }
    
    @property
    def MAX_RAM(self):
        return 64
    
    @property
    def computer_type(self):
        return "laptop"
    
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
    
