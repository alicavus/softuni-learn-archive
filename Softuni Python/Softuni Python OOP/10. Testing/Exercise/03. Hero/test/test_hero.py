from project.hero import Hero
from unittest import TestCase, main

class HeroTest(TestCase):
    def setUp(self):
        self.hero = Hero("InesIvanova", 2, 1, 0.1)
    
    def test_constructor_data(self):
        self.assertEqual("InesIvanova", self.hero.username)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(1, self.hero.health)
        self.assertEqual(0.1, self.hero.damage)
    
    def test_battle_fight_yourself(self):
        with self.assertRaises(Exception) as ctx:
            self.hero.battle(Hero(self.hero.username, 99, 99, 99))
        self.assertEqual(ctx.exception.__str__(), "You cannot fight yourself")
    
    def test_battle_you_need_rest_health_negative(self):
        self.hero.health = -99
        with self.assertRaises(ValueError) as ctx:
            self.hero.battle(Hero("Diablo", 99, 99, 99))
        self.assertEqual(ctx.exception.__str__(), "Your health is lower than or equal to 0. You need to rest")
    
    def test_battle_you_need_rest_health_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ctx:
            self.hero.battle(Hero("Diablo", 99, 99, 99))
        self.assertEqual(ctx.exception.__str__(), "Your health is lower than or equal to 0. You need to rest")
    
    def test_battle_enemy_need_rest_health_negative(self):
        with self.assertRaises(ValueError) as ctx:
            self.hero.battle(Hero("Diablo", 99, -8, 99))
        self.assertEqual(ctx.exception.__str__(), "You cannot fight Diablo. He needs to rest")
    
    def test_battle_enemy_need_rest_health_zero(self):
        with self.assertRaises(ValueError) as ctx:
            self.hero.battle(Hero("Diablo", 99, 0, 99))
        self.assertEqual(ctx.exception.__str__(), "You cannot fight Diablo. He needs to rest")
    
    def test_battle_draw(self):
        self.hero = Hero("Cow", 2, 1, 1)
        result = self.hero.battle(Hero("Diablo", 2, 1, 1))
        expected_result = "Draw"
        self.assertEqual(result, expected_result)
    
    def test_battle_win(self):
        self.hero = Hero("Cow", 2, 12, 1)
        result = self.hero.battle(Hero("Diablo", 2, 1, 1))
        expected_result = "You win"
        self.assertEqual(result, expected_result)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(15, self.hero.health)
        self.assertEqual(6, self.hero.damage)
    
    def test_battle_lost(self):
        self.hero = Hero("Cow", 2, 12, 1)
        enemy = Hero("Diablo", 2, 21, 1)
        result = self.hero.battle(enemy)
        expected_result = "You lose"
        self.assertEqual(result, expected_result)
        self.assertEqual(3, enemy.level)
        self.assertEqual(24, enemy.health)
        self.assertEqual(6, enemy.damage)
    
    def test_str(self):
        self.assertEqual(str(self.hero), "Hero InesIvanova: 2 lvl\nHealth: 1\nDamage: 0.1\n")


if __name__ == "__main__":
    main()