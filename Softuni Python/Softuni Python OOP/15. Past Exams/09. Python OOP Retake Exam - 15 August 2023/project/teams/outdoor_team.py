from project.teams.base_team import BaseTeam

class OutdoorTeam(BaseTeam):
    @property
    def _data(self) -> dict:
        return {
            "initial budget": 1_000.0,
            "increase advantage": 115
        }
    
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self._data.get("initial budget", 0))
