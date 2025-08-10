from project.collectors.base_collector import BaseCollector

class PrivateCollector(BaseCollector):
    def __init__(self, name: str):
        super().__init__(name, self.DATA["available money"], self.DATA["available space"])

    @property
    def DATA(self):
        return {
            "available money": 25_000.0,
            "available space": 3_000,
            "increase money": 5_000.0
        }