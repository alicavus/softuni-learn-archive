class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name: str = name
        self.__sprint: int = sprint
        self.__dribble: int = dribble
        self.__passing: int = passing
        self.__shooting: int = shooting
    
    @property
    def name(self) -> str:
        return self.__name
    
    def __str__(self):
        return "\n".join(
            [
            f"Player: {self.name}",
            f"Sprint: {self.__sprint}",
            f"Dribble: {self.__dribble}",
            f"Passing: {self.__passing}",
            f"Shooting: {self.__shooting}"
            ]
        )
    