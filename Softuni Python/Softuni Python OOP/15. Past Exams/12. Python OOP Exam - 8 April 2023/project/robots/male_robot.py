from project.robots.base_robot import BaseRobot

class MaleRobot(BaseRobot):
    @property
    def _data(self) -> dict:
        return {
            "initial weight": 9,
            "increase weight": 3
        }
    
    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self._data.get("initial weight", 0))
    

