from project.clients.base_client import BaseClient

class RegularClient(BaseClient):
    MEMBERSHIP_TYPE = "Regular"
    def __init__(self, name: str):
        super().__init__(name, self.MEMBERSHIP_TYPE)

    @property
    def _points_multiplier(self) -> float:
        return 0.1


