from project.player import Player

class Team:
    def __init__(self, name: str, rating: int):
        self.__name: str = name
        self.__rating: int = rating
        self.__players: list[Player] = []

    def add_player(self, player: Player) -> str:
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players += [player]
        return f"Player {player.name} joined team {self.__name}"
    
    def remove_player(self, player_name: str) -> Player | str:
        for idx, player in enumerate(self.__players):
            if player.name == player_name:
                self.__players.pop(idx)
                return player
        return f"Player {player_name} not found"


