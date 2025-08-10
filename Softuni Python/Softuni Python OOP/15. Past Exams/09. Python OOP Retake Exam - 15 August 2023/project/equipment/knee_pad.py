from project.equipment.base_equipment import BaseEquipment

class KneePad(BaseEquipment):
    @property
    def _data(self) -> dict:
        return {
            "protection": 120,
            "price": 15.0,
            "increase rate": 0.2
        }
    
    def __init__(self):
        super().__init__(self._data.get("protection", 0), self._data.get("price", 0))
    