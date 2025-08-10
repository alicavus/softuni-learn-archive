class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

import unittest
class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Jo Garcia", 50_000, 100)
    
    def test_correct_name(self):
        result = self.worker.name
        expected_result = "Jo Garcia"
        self.assertEqual(result, expected_result)
    
    def test_correct_salary(self):
        result = self.worker.salary
        expected_result = 50_000
        self.assertEqual(result, expected_result)
    
    def test_correct_energy(self):
        result = self.worker.energy
        expected_result = 100
        self.assertEqual(result, expected_result)
    
    def test_energy_incremented_after_rest(self):
        pre_rest_energy = self.worker.energy
        self.worker.rest()
        post_rest_energy = self.worker.energy
        self.assertEqual(pre_rest_energy + 1, post_rest_energy)
    
    def test_error_work_negative_energy(self):
        self.worker.energy = -3
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')
    
    def test_error_work_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')
    
    def test_money_increased_salary_after_work(self):
        pre_money = self.worker.money
        self.worker.work()
        post_money = self.worker.money
        self.assertEqual(pre_money + self.worker.salary, post_money)
    
    def test_energy_decreased_after_work(self):
        pre_energy = self.worker.energy
        self.worker.work()
        post_energy = self.worker.energy
        self.assertEqual(post_energy + 1, pre_energy)
    
    def test_get_info(self):
        self.worker.work()
        result = self.worker.get_info()
        expected = "Jo Garcia has saved 50000 money."
        self.assertEqual(result, expected)
    
if __name__ == "__main__":
    unittest.main()