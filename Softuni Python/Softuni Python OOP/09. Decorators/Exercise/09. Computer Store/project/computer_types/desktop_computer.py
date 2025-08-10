from project.computer_types.computer import Computer

class DesktopComputer(Computer):
    @property
    def CPU(self):
        return {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800        
        }
    
    @property
    def MAX_RAM(self):
        return 128
    
    @property
    def computer_type(self):
        return "desktop computer"
    

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
