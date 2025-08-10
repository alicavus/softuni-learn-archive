from project.clients.base_client import BaseClient


class Adult(BaseClient):
    @property
    def _data(self) -> dict:
        return {
            "initial interest": 4.0,
            "increase interest": 2.0
        }

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self._data.get("initial interest", 0))
