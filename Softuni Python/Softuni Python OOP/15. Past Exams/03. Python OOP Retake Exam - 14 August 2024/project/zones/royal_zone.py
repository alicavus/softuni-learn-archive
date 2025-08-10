from project.zones.base_zone import BaseZone

class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10
    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def __str__(self):
        return "Royal Zone"


