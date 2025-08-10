from project.f1_season_app import F1SeasonApp
f1_season = F1SeasonApp()

print(f1_season.register_team_for_season("Red Bull", 2000000))
print(f1_season.register_team_for_season("Mercedes", 2500000))
print(f1_season.new_race_results("Nurburgring", 1, 7))
print(f1_season.new_race_results("Silverstone", 10, 1))

from project import *
team_names = {
            "Red Bull": {
                "class": RedBullTeam,
                "attribute": "red_bull_team"
            },
            "Mercedes": {
                "class":  MercedesTeam,
                "attribute": "mercedes_team"
            }
        }

print(team_names["Red Bull"])

