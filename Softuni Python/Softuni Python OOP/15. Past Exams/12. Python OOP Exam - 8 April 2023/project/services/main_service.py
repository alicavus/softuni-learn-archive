from project.services.base_service import BaseService

class MainService(BaseService):
    @property
    def _data(self) -> dict:
        return {
            "capacity": 30,
            "service type": "Main Service"
        }
    
    def __init__(self, name: str):
        super().__init__(name, self._data.get("capacity", 0))