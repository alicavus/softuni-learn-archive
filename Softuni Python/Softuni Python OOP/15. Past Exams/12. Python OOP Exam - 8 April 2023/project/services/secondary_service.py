from project.services.base_service import BaseService

class SecondaryService(BaseService):
    @property
    def _data(self) -> dict:
        return {
            "capacity": 15,
            "service type": "Secondary Service"
        }
    
    def __init__(self, name: str):
        super().__init__(name, self._data.get("capacity", 0))