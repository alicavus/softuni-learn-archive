from project.formula_teams.formula_team import FormulaTeam

class MercedesTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)
        self.expences = 200_000
        self.sponsors = {
            "Petronas": {
                1: 1_000_000,
                3: 500_000
            },
            "TeamViewer": {
                5: 100_000,
                7: 50_000
            }
        }
    
    def calculate_revenue_after_race(self, race_pos):
        return super().calculate_revenue_after_race(race_pos)