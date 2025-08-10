from project.clients.base_client import BaseClient

class VIPClient(BaseClient):
    MEMBERSHIP_TYPE = "VIP"
    def __init__(self, name: str):
        super().__init__(name, self.MEMBERSHIP_TYPE)

    @property
    def _points_multiplier(self) -> float:
        return 0.2