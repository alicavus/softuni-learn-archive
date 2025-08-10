from project.formula_teams.formula_team import FormulaTeam

class RedBullTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)
        self.expences = 250_000
        self.sponsors = {
            "Oracle": {
                1: 1_500_000,
                2: 800_000
            },
            "Honda": {
                8: 20_000,
                10: 10_000
            }
        }
    
    def calculate_revenue_after_race(self, race_pos):
        return super().calculate_revenue_after_race(race_pos)