from project.soccer_player import SoccerPlayer
from unittest import TestCase, main

class TestSoccerPlayer(TestCase):
    def setUp(self):
        self.player = SoccerPlayer("Arda Güler", 20, 123, "Real Madrid")
    
    def test_initialisation(self):
        #value asserts
        self.assertEqual("Arda Güler", self.player._SoccerPlayer__name)
        self.assertEqual(20, self.player._SoccerPlayer__age)
        self.assertEqual(123, self.player._SoccerPlayer__goals)
        self.assertEqual("Real Madrid", self.player._SoccerPlayer__team)
        self.assertEqual({}, self.player.achievements)

        #type asserts
        self.assertIsInstance(self.player._SoccerPlayer__name, str)
        self.assertIsInstance(self.player._SoccerPlayer__age, int)
        self.assertIsInstance(self.player._SoccerPlayer__goals, int)
        self.assertIsInstance(self.player._SoccerPlayer__team, str)
        self.assertIsInstance(self.player.achievements, dict)
    
    def test_properties(self):
        self.assertEqual(self.player.name, self.player._SoccerPlayer__name)
        self.assertEqual(self.player.age, self.player._SoccerPlayer__age)
        self.assertEqual(self.player.goals, self.player._SoccerPlayer__goals)
        self.assertEqual(self.player.team, self.player._SoccerPlayer__team)
    
    def test_name_setter_name_less_than_six_symbols(self):
        with self.assertRaises(ValueError) as ctx:
            self.player.name = "J"
        self.assertEqual("Name should be more than 5 symbols!", ctx.exception.__str__())
    
    def test_name_setter_name_ok(self):
        self.player.name = "Valeri Bozhinoff"
        self.assertEqual("Valeri Bozhinoff", self.player._SoccerPlayer__name)
    
    def test_age_setter_age_less_than_legal_age(self):
        with self.assertRaises(ValueError) as ctx:
            self.player.age = 13
        self.assertEqual("Players must be at least 16 years of age!", ctx.exception.__str__())
    
    def test_age_setter_age_ok(self):
        self.player.age = 16
        self.assertEqual(16, self.player._SoccerPlayer__age)
    
    def test_goals_setter(self):
        self.player.goals = -13
        self.assertEqual(0, self.player._SoccerPlayer__goals)
        self.player.goals = 0
        self.assertEqual(0, self.player._SoccerPlayer__goals)
        self.player.goals = 155
        self.assertEqual(155, self.player._SoccerPlayer__goals)
    
    def test_team_setter_invalid_team(self):
        with self.assertRaises(ValueError) as ctx:
            self.player.team = "Fenerbahçe"
        self.assertEqual("Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!", ctx.exception.__str__())
    
    def test_team_setter_valid_team(self):
        for team in ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"]:
            self.player.team = team
            self.assertEqual(team, self.player._SoccerPlayer__team)
    
    def test_change_team(self):
        self.assertEqual("Invalid team name!", self.player.change_team("Fenerbahçe"))
        for team in ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"]:
            self.assertEqual("Team successfully changed!", self.player.change_team(team))
    
    def test_add_new_achievement(self):
        achievements = [f"Achievement {number}" for number in range(1, 10)]
        self.assertEqual({}, self.player.achievements)
        for achievement in achievements:
            self.assertNotIn(achievement, self.player.achievements)
            res = self.player.add_new_achievement(achievement)
            self.assertIn(achievement, self.player.achievements)
            self.assertEqual(f"{achievement} has been successfully added to the achievements collection!", res)
            self.assertEqual(1, self.player.achievements[achievement])

            self.player.add_new_achievement(achievement)
            self.assertEqual(2, self.player.achievements[achievement])
        self.assertEqual({achievement: 2 for achievement in achievements}, self.player.achievements)
    
    def test__lt__(self):
        player = SoccerPlayer("Carlos Henrique Casimiro", 33, 213, "Real Madrid")
        player2 = SoccerPlayer("Valeri Bojinov", 33, 123, "PSG")
        result1 = self.player < player
        result2 = self.player > player
        result3 = self.player < player2
        expected1 = "Carlos Henrique Casimiro is a top goal scorer! S/he scored more than Arda Güler."
        expected2 = "Carlos Henrique Casimiro is a better goal scorer than Arda Güler."
        expected3 = "Arda Güler is a better goal scorer than Valeri Bojinov."
        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)
        self.assertEqual(expected3, result3)

if __name__ == "__main__":
    main()
