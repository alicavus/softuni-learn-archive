from project.battleships.base_battleship import BaseBattleship

class RoyalBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 100
    REDUCE_AMMUNITION = 25
    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.INITIAL_AMMUNITION)

    def __str__(self):
        return "Royal Battleship"