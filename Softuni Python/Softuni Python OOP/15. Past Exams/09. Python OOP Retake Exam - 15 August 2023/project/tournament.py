from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam

class Tournament:
    VALID_EQUIPEMENTS = {
       "ElbowPad": ElbowPad,
       "KneePad": KneePad
    }
    VALID_TEAMS = {
        "IndoorTeam": IndoorTeam,
        "OutdoorTeam": OutdoorTeam
    }
    def __init__(self, name: str, capacity: int):
        self.name: str = name
        self.capacity: int = capacity
        self.equipment: list[BaseEquipment] = []
        self.teams: list[BaseTeam] = []
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self._name: str = value
    
    def add_equipment(self, equipment_type: str):
        cls = self.VALID_EQUIPEMENTS.get(equipment_type, None)

        if cls is None:
            raise Exception("Invalid equipment type!")
        
        self.equipment.append(cls())
        return f"{equipment_type} was successfully added."
    
    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        cls = self.VALID_TEAMS.get(team_type, None)
        if cls is None:
            raise Exception("Invalid team type!")
        
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."
        
        self.teams.append(cls(team_name, country, advantage))
        return f"{team_type} was successfully added."
    
    def sell_equipment(self, equipment_type: str, team_name: str):
        team: BaseTeam = self.get_item(self.teams, "name", team_name)
        equipment: BaseEquipment = self.get_item(reversed(self.equipment), "__class__", self.VALID_EQUIPEMENTS.get(equipment_type, None))

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        
        team.budget -= equipment.price
        team.equipment.append(equipment)
        self.equipment.remove(equipment)

        return f"Successfully sold {equipment_type} to {team_name}."
    
    def remove_team(self, team_name: str):
        team: BaseTeam = self.get_item(self.teams, "name", team_name)
        if team is None:
            raise Exception("No such team!")
        
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        
        self.teams.remove(team)
        return f"Successfully removed {team_name}."
    
    def increase_equipment_price(self, equipment_type: str):
        count = 0
        for equipment in self.equipment:
            if equipment.__class__ == self.VALID_EQUIPEMENTS.get(equipment_type, None):
                equipment.increase_price()
                count += 1
        
        return f"Successfully changed {count}pcs of equipment."
    
    def play(self, team_name1: str, team_name2: str):
        team_one: BaseTeam = self.get_item(self.teams, "name", team_name1)
        team_two: BaseTeam = self.get_item(self.teams, "name", team_name2)

        if not team_one or not team_two:
            return
        
        if team_one.__class__ != team_two.__class__:
            raise Exception("Game cannot start! Team types mismatch!")
        
        sum_team_one = team_one.equipement_stats.get("protection", 0) + team_one.advantage
        sum_team_two = team_two.equipement_stats.get("protection", 0) + team_two.advantage

        winner = team_one if sum_team_one > sum_team_two else team_two if sum_team_one < sum_team_two else None

        if winner is None:
            return "No winner in this game."
        
        winner.win()
        return f"The winner is {winner.name}."
    
    def get_statistics(self) -> str:
        result = [
            f"Tournament: {self.name}",
            f"Number of Teams: {len(self.teams)}",
            f"Teams:"
        ]

        result.extend(
            team.get_statistics() for team in sorted(self.teams, key=lambda t: -t.wins)
        )

        return "\n".join(result)
    
    @staticmethod
    def get_item(collection, attribute_name, attribute_value):
        return next((item for item in collection if getattr(item, attribute_name, None) == attribute_value), None)
        


    
    