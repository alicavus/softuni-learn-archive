from CarManager.car_manager import Car

import unittest

class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car("Skoda", "Fabia", 3, 53)
    
    def test_constructor(self):
        self.assertEqual(self.car._Car__make, "Skoda")
        self.assertEqual(self.car._Car__model, "Fabia")
        self.assertEqual(self.car._Car__fuel_consumption, 3)
        self.assertEqual(self.car._Car__fuel_capacity, 53)
        self.assertEqual(self.car._Car__fuel_amount, 0)
    
    def test_instance_properties(self):
        self.assertEqual(self.car.make, "Skoda")
        self.assertEqual(self.car.model, "Fabia")
        self.assertEqual(self.car.fuel_consumption, 3)
        self.assertEqual(self.car.fuel_capacity, 53)
        self.assertEqual(self.car.fuel_amount, 0)
    
    def test_make_setter_valid(self):
        self.car.make = "Zkoda"
        self.assertEqual(self.car.make, "Zkoda")
    
    def test_make_setter_invalid(self):
        with self.assertRaises(Exception) as ctx:
            self.car.make = ""
        self.assertEqual(str(ctx.exception), "Make cannot be null or empty!")
    
    def test_model_setter_valid(self):
        self.car.model = "Zkoda"
        self.assertEqual(self.car.model, "Zkoda")
    
    def test_model_setter_invalid(self):
        with self.assertRaises(Exception) as ctx:
            self.car.model = ""
        self.assertEqual(str(ctx.exception), "Model cannot be null or empty!")
    
    def test_fuel_consumption_setter_valid(self):
        self.car.fuel_consumption = 8
        self.assertEqual(self.car.fuel_consumption, 8)
    
    def test_fuel_consumption_setter_invalid(self):
        with self.assertRaises(Exception) as ctx:
            self.car.fuel_consumption = 0
        self.assertEqual(str(ctx.exception), "Fuel consumption cannot be zero or negative!")
        with self.assertRaises(Exception) as ctx:
            self.car.fuel_consumption = -2
        self.assertEqual(str(ctx.exception), "Fuel consumption cannot be zero or negative!")
    
    def test_fuel_capacity_setter_valid(self):
        self.car.fuel_capacity = 8
        self.assertEqual(self.car.fuel_capacity, 8)
    
    def test_fuel_capacity_setter_invalid(self):
        with self.assertRaises(Exception) as ctx:
            self.car.fuel_capacity = 0
        self.assertEqual(str(ctx.exception), "Fuel capacity cannot be zero or negative!")
        with self.assertRaises(Exception) as ctx:
            self.car.fuel_capacity = -2
        self.assertEqual(str(ctx.exception), "Fuel capacity cannot be zero or negative!")
    
    def test_fuel_amount_setter_valid(self):
        self.car.fuel_amount = 8
        self.assertEqual(self.car.fuel_amount, 8)
    
    def test_fuel_amount_setter_invalid(self):
        with self.assertRaises(Exception) as ctx:
            self.car.fuel_amount = -2
        self.assertEqual(str(ctx.exception), "Fuel amount cannot be negative!")
    
    def test_refuel_fuel_amount_zero(self):
        with self.assertRaises(Exception) as ctx:
            self.car.refuel(0)
        self.assertEqual(str(ctx.exception), "Fuel amount cannot be zero or negative!")
    
    def test_refuel_fuel_amount_negative(self):
        with self.assertRaises(Exception) as ctx:
            self.car.refuel(-8)
        self.assertEqual(str(ctx.exception), "Fuel amount cannot be zero or negative!")
    
    def test_refuel_fuel_amount_less_capacity(self):
        fuel_amount_before = self.car.fuel_amount
        self.car.refuel(15)
        fuel_amount_after = self.car.fuel_amount
        self.assertEqual(fuel_amount_before + 15, fuel_amount_after)
    
    def test_refuel_fuel_amount_more_capacity(self):
        self.car.refuel(1000)
        result = self.car.fuel_amount
        expected_result = self.car.fuel_capacity
        self.assertEqual(result, expected_result)
    
    def test_drive_enough_fuel(self):
        self.car.refuel(3)
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 0)
    
    def test_drive_not_enough_fuel(self):
        self.car.refuel(1)
        with self.assertRaises(Exception) as ctx:
            self.car.drive(100)
        self.assertEqual(str(ctx.exception), "You don't have enough fuel to drive!")

if __name__ == "__main__":
    unittest.main()