from project.collectors.base_collector import BaseCollector

class Museum(BaseCollector):
    def __init__(self, name: str):
        super().__init__(name, self.DATA["available money"], self.DATA["available space"])

    @property
    def DATA(self):
        return {
            "available money": 15_000.0,
            "available space": 2_000,
            "increase money": 1_000.0
        }

    

    
