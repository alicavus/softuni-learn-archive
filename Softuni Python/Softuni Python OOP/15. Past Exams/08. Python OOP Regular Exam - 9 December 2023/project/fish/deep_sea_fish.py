from project.fish.base_fish import BaseFish

class DeepSeaFish(BaseFish):
    @property
    def TIME_TO_CATCH(self):
        return 180
    def __init__(self, name: str, points: float):
        super().__init__(name, points, self.TIME_TO_CATCH)