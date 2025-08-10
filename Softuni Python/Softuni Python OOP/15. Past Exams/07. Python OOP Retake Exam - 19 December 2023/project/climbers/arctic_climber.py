from project.climbers.base_climber import BaseClimber

class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200
    def __init__(self, name: str):
        super().__init__(name, self.__class__.INITIAL_STRENGTH)
    
    @property
    def _data(self) -> dict:
        return {
            "required climbing strength": 100,
            "reduced by": 20,
            "multiplied by": (1.5, 2.0, "Extreme")
        }