from project.player import Player

class Guild:
    def __init__(self, name: str):
        self.name: str = name
        self.players: list[Player] = []
    
    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        
        player.guild = self.name
        self.players += [player]
        return f"Welcome player {player.name} to the guild {self.name}"
    
    def kick_player(self, player_name: str) -> str:
        for idx, player in enumerate(self.players):
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.pop(idx)
                return f"Player {player_name} has been removed from the guild."
        
        return f"Player {player_name} is not in the guild."
            
    
    def guild_info(self) -> str:
        result: list[str] = [f"Guild: {self.name}"]
        for player in self.players:
            result += [player.player_info()]
        return "\n".join(result)

