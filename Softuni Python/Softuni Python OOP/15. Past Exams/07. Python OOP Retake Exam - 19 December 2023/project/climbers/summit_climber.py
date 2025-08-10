from project.climbers.base_climber import BaseClimber

class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150
    def __init__(self, name: str):
        super().__init__(name, self.__class__.INITIAL_STRENGTH)
    
    @property
    def _data(self) -> dict:
        return {
            "required climbing strength": 75,
            "reduced by": 30,
            "multiplied by": (2.5, 1.3, "Advanced")
        }