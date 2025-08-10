from project.tennis_player import TennisPlayer
from unittest import main, TestCase

class TestTennisPlayerClass(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Grigor Nadal", 21, 123.45)
    
    def test_initialisation_data(self):
        self.assertEqual("Grigor Nadal", self.player.name)
        self.assertEqual(21, self.player.age)
        self.assertEqual(123.45, self.player.points)
        self.assertEqual([], self.player.wins)

        self.assertIsInstance(self.player.name, str)
        self.assertIsInstance(self.player.age, int)
        self.assertIsInstance(self.player.points, float)
        self.assertIsInstance(self.player.wins, list)
    
    def test_name_setter_value_length_less_than_eq_to_two_should_rise_error(self):
        for name in "", "aa", " a":
            with self.assertRaises(ValueError) as e:
                self.player.name = name
            self.assertEqual("Name should be more than 2 symbols!", e.exception.args[0])
    
    def test_name_setter_value_length_more_than_two_will_set_name(self):
        for name in "Grigor Nadal", "abc", "Novak Dimitroff":
            self.player.name = name
            self.assertEqual(name, self.player.name)
    
    def test_age_setter_value_less_than_legal_age_should_rise_error(self):
        for age in -2, 0, 10, 17:
            with self.assertRaises(ValueError) as e:
                self.player.age = age
            self.assertEqual("Players must be at least 18 years of age!", e.exception.args[0])
    
    def test_age_setter_value_at_legal_age_should_set_age(self):
        for age in 18, 21, 25, 33, 67, 99:
            self.player.age = age
            self.assertEqual(age, self.player.age)
    
    def test_add_new_win_new_tournnament_should_append_to_wins(self):
        wins = [f"Tournament {n}" for n in range(1, 100)]
        for n, win in enumerate(wins, 1):
            result = self.player.add_new_win(win)
            self.assertEqual(self.player.wins, wins[:n])
            self.assertIsNone(result)
    
    def test_add_new_win_existing_tournnament_should_not_append_to_wins(self):
        wins = [f"Tournament {n}" for n in range(1, 100)]
        
        for win in wins:
            self.player.add_new_win(win)

        for win in wins:
            result = self.player.add_new_win(win)
            self.assertEqual(self.player.wins, wins)
            self.assertEqual(f"{win} has been already added to the list of wins!", result)

    def test__lt__other_player_points_are_higher(self):
        player = TennisPlayer("Tennis Player", 32, 123.46)
        result = self.player < player
        expected = "Tennis Player is a top seeded player and he/she is better than Grigor Nadal"
        self.assertEqual(expected, result)

    def test__lt__other_player_points_are_equal(self):
        player = TennisPlayer("Tennis Player", 32, 123.45)
        result = self.player < player
        expected = "Grigor Nadal is a better player than Tennis Player"
        self.assertEqual(expected, result)

    def test__lt__other_player_points_are_lower(self):
        player = TennisPlayer("Tennis Player", 32, 123.43)
        result = self.player < player
        expected = "Grigor Nadal is a better player than Tennis Player"
        self.assertEqual(expected, result)
    
    def test__str__no_wins(self):
        self.assertEqual("Tennis Player: Grigor Nadal\nAge: 21\nPoints: 123.5\nTournaments won: ", str(self.player))
    
    def test__str__one_tournament_wins(self):
        self.player.add_new_win("Tournament 1")
        self.assertEqual("Tennis Player: Grigor Nadal\nAge: 21\nPoints: 123.5\nTournaments won: Tournament 1", str(self.player))

    def test__str___more_than_one_tournament_wins(self):
        self.player.add_new_win("Tournament 1")
        self.player.add_new_win("Tournament 2")
        self.assertEqual("Tennis Player: Grigor Nadal\nAge: 21\nPoints: 123.5\nTournaments won: Tournament 1, Tournament 2", str(self.player))



if __name__ == "__main__":
    main()