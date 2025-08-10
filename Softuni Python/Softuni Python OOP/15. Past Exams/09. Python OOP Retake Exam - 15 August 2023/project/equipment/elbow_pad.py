from project.equipment.base_equipment import BaseEquipment

class ElbowPad(BaseEquipment):
    @property
    def _data(self) -> dict:
        return {
            "protection": 90,
            "price": 25.0,
            "increase rate": 0.1
        }
    
    def __init__(self):
        super().__init__(self._data.get("protection", 0), self._data.get("price", 0))
    