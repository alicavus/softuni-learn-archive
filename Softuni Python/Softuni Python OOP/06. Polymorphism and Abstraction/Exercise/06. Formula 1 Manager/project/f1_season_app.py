from project.formula_teams import FormulaTeam, RedBullTeam, MercedesTeam

class F1SeasonApp:
    def __init__(self):
        self.red_bull_team: RedBullTeam = None
        self.mercedes_team: MercedesTeam = None
        self.team_names = {
            "Red Bull": {
                "class": RedBullTeam,
                "attribute": "red_bull_team"
            },
            "Mercedes": {
                "class":  MercedesTeam,
                "attribute": "mercedes_team"
            }
        }
    
    def register_team_for_season(self, team_name: str, budget: int):
        try:
            team_info = self.team_names[team_name]
            team_instance = team_info["class"](budget)

            setattr(self, team_info["attribute"], team_instance)
            
        except KeyError:
            raise ValueError("Invalid team name!")
        
        else:
            return f"{ team_name } has joined the new F1 season."
    
    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.mercedes_team or not self.red_bull_team:
            raise Exception("Not all teams have registered for the season.")
        return f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. {'Mercedes' if mercedes_pos < red_bull_pos else 'Red Bull'} is ahead at the {race_name} race."

