from project.robots.base_robot import BaseRobot

class FemaleRobot(BaseRobot):
    @property
    def _data(self) -> dict:
        return {
            "initial weight": 7,
            "increase weight": 1
        }
    
    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self._data.get("initial weight", 0))
    

