from project.robot import Robot
from unittest import main, TestCase

class TestRobotClass(TestCase):
    def setUp(self):
        self.allowed_categories = ['Military', 'Education', 'Entertainment', 'Humanoids']
        self.price_increment = 1.5
        self.robot = Robot("1234A", 'Education', 990, 1_000.0)

    def test_constructors(self):
        for cat in self.allowed_categories:
            robot = Robot("12345A", cat, 100, 500.0)
            self.assertEqual("12345A", robot.robot_id)
            self.assertEqual(cat, robot.category)
            self.assertEqual(100, robot.available_capacity)
            self.assertEqual(500.0, robot.price)
            self.assertEqual([], robot.hardware_upgrades)
            self.assertEqual([], robot.software_updates)

    def test_category_setter_wrong_category(self):
        for cat in (f"Random category {n}" for n in range(1, 100)):
            with self.assertRaises(ValueError) as e:
                self.robot.category = cat
            self.assertEqual(f"Category should be one of '{self.allowed_categories}'", e.exception.args[0])
            self.assertNotEqual(cat, self.robot.category)

    def test_category_setter_allowed_category(self):
        for cat in self.allowed_categories:
            self.robot.category = cat
            self.assertEqual(cat, self.robot.category)

    def test_price_setter_negative_value(self):
        for price in -45.0, -11, -1, -0.01:
            with self.assertRaises(ValueError) as e:
                self.robot.price = price
            self.assertEqual("Price cannot be negative!", e.exception.args[0])
            self.assertNotEqual(price, self.robot.price)

    def test_price_setter_non_negative_value(self):
        for price in 0.0, 0, 0.01, 100.0, 123.23, 10_000:
            self.robot.price = price
            self.assertEqual(price, self.robot.price)

    def test_upgrade_hardware_component_existent_in_upgraded_lists(self):
        components = [f"Component {n}" for n in range(1, 100)]
        self.robot.hardware_upgrades = [c for c in components]
        price = self.robot.price
        for c in components:
            result = self.robot.upgrade(c, 123.23)
            self.assertEqual(f"Robot {self.robot.robot_id} was not upgraded.", result)
            self.assertEqual(price, self.robot.price)

    def test_upgrade_hardware_component_non_existent_in_upgraded_lists(self):
        components = [f"Component {n}" for n in range(1, 100)]
        for c in components:
            price = self.robot.price
            result = self.robot.upgrade(c, 123.23)
            expected = price + 123.23 * self.price_increment
            self.assertEqual(f'Robot {self.robot.robot_id} was upgraded with {c}.', result)
            self.assertEqual(expected, self.robot.price)
            self.assertIn(c, self.robot.hardware_upgrades)

    def test_update_insufficient_capacity(self):
        capacity = self.robot.available_capacity
        for inc in 1, 2, 265, 512:
            result = self.robot.update(inc * 0.01, capacity + inc)
            self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)
            self.assertNotIn(inc * 0.01, self.robot.software_updates)

    def test_update_insufficient_version(self):
        capacity = self.robot.available_capacity
        updates = [v * 0.01 for v in [1, 2, 265, 512]]
        self.robot.software_updates = [u for u in updates]
        for update in updates:
            result = self.robot.update(update, 1)
            self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)
            self.assertEqual(1, self.robot.software_updates.count(update))
            self.assertEqual(capacity, self.robot.available_capacity)

    def test_update_ok(self):
        updates = {f"Update {n}": n for n in range(1, 45)}
        for update in updates:
            capacity = self.robot.available_capacity
            value = updates[update]
            version = value * 0.01
            result = self.robot.update(version, value)
            self.assertEqual(f'Robot {self.robot.robot_id} was updated to version {version}.', result)
            self.assertIn(version, self.robot.software_updates)
            self.assertEqual(capacity - value, self.robot.available_capacity)

    def test__gt__(self):
        robot = Robot(self.robot.robot_id.replace("A", "B"), self.robot.category, self.robot.available_capacity, self.robot.price - 0.01)
        self.assertEqual(f"Robot with ID {self.robot.robot_id} is more expensive than Robot with ID {robot.robot_id}.", self.robot > robot)

        robot = Robot(self.robot.robot_id.replace("A", "B"), self.robot.category, self.robot.available_capacity, self.robot.price)
        self.assertEqual(f"Robot with ID {self.robot.robot_id} costs equal to Robot with ID {robot.robot_id}.", self.robot > robot)

        robot = Robot(self.robot.robot_id.replace("A", "B"), self.robot.category, self.robot.available_capacity, self.robot.price + 0.01)
        self.assertEqual(f"Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {robot.robot_id}.", self.robot > robot)







if __name__ == "__main__":
    main()