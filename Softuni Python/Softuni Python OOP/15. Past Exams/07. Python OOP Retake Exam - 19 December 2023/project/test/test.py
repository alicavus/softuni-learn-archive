from project.climbing_robot import ClimbingRobot
import unittest

class TestClimbingRobotClass(unittest.TestCase):
    def setUp(self):
        self.robot = ClimbingRobot('Alpine', 'Part Type', 128, 256)

    def test_initialisation_data(self):
        self.assertEqual('Alpine', self.robot.category)
        self.assertEqual('Part Type', self.robot.part_type)
        self.assertEqual(128, self.robot.capacity)
        self.assertEqual(256, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_property(self):
        self.assertTrue(isinstance(getattr(ClimbingRobot, "category"), property))
        self.assertTrue(self.robot._ClimbingRobot__category, self.robot.category)

    def test_category_setter_not_from_list(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "Invalid"
        self.assertEqual("Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']", str(ex.exception))

    def test_category_setter_valid(self):
        for category in ['Mountain', 'Alpine', 'Indoor', 'Bouldering']:
            self.robot.category = category
            self.assertEqual(category, self.robot.category)

    def test_get_used_capacity(self):
        self.assertEqual(0, self.robot.get_used_capacity())
        for capacity in [20, 50, 80, 100, 128]:
            self.robot.installed_software = [{'capacity_consumption': capacity - 8 }, {'capacity_consumption': 8}]
            self.assertEqual(capacity, self.robot.get_used_capacity())

    def test_get_available_capacity(self):
        self.assertEqual(128, self.robot.get_available_capacity())
        for capacity in [20, 50, 80, 100, 128]:
            self.robot.installed_software = [{'capacity_consumption': capacity - 8 }, {'capacity_consumption': 8}]
            self.assertEqual(128 - capacity, self.robot.get_available_capacity())

    def test_get_used_memory(self):
        self.assertEqual(0, self.robot.get_used_memory())
        for memory in [20, 85, 180, 201, 240, 256]:
            self.robot.installed_software = [{'memory_consumption': memory - 16 }, {'memory_consumption': 16}]
            self.assertEqual(memory, self.robot.get_used_memory())

    def test_get_available_memory(self):
        self.assertEqual(256, self.robot.get_available_memory())
        for memory in [20, 85, 180, 201, 240, 256]:
            self.robot.installed_software = [{'memory_consumption': memory - 25 }, {'memory_consumption': 25}]
            self.assertEqual(256 - memory, self.robot.get_available_memory())

    def test_install_software_success(self):
        for software in [{'name': f'Software {idx}', 'memory_consumption': 64, 'capacity_consumption': 32} for idx in range(1, 5)]:
            result = self.robot.install_software(software)
            expected = f"Software '{software['name']}' successfully installed on {self.robot.category} part."
            self.assertEqual(expected, result)
            self.assertIn(software, self.robot.installed_software)

    def test_install_software_failure_memory(self):
        software = {'name': 'Test software failure', 'memory_consumption': self.robot.memory + 1, 'capacity_consumption': self.robot.capacity - 1}
        result = self.robot.install_software(software)
        expected = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        self.assertEqual(expected, result)
        self.assertNotIn(software, self.robot.installed_software)

    def test_install_software_failure_capacity(self):
        software = {'name': 'Test software failure', 'memory_consumption': self.robot.memory - 10, 'capacity_consumption': self.robot.capacity + 1}
        result = self.robot.install_software(software)
        expected = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        self.assertEqual(expected, result)
        self.assertNotIn(software, self.robot.installed_software)

    def test_install_software_failure_memory_and_capacity(self):
        software = {'name': 'Test software failure', 'memory_consumption': self.robot.memory + 1, 'capacity_consumption': self.robot.capacity + 1}
        result = self.robot.install_software(software)
        expected = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."
        self.assertEqual(expected, result)
        self.assertNotIn(software, self.robot.installed_software)







if __name__ == '__main__':
    unittest.main()