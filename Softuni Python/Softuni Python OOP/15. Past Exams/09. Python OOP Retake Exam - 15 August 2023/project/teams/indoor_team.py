from project.teams.base_team import BaseTeam

class IndoorTeam(BaseTeam):
    @property
    def _data(self) -> dict:
        return {
            "initial budget": 500.0,
            "increase advantage": 145
        }
    
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self._data.get("initial budget", 0))
