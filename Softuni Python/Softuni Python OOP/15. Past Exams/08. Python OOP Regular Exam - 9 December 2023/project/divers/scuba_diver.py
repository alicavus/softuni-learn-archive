from project.divers.base_diver import BaseDiver

class ScubaDiver(BaseDiver):
    @property
    def _data(self):
        return {
            "default oxygen level": 540,
            "miss percent": 0.3
        }

    def __init__(self, name: str):
        super().__init__(name, self._data.get("default oxygen level", 0))