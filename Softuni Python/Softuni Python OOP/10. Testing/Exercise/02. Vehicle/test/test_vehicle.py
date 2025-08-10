from project.vehicle import Vehicle
from unittest import TestCase, main

class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 101)
    
    def test_constructor(self):
        self.assertEqual(self.vehicle.fuel, 100)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(self.vehicle.horse_power, 101)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)
    
    def test_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as ctx:
            self.vehicle.drive(500)
        self.assertEqual(ctx.exception.__str__(), "Not enough fuel")
    
    def test_drive_enough_fuel(self):
        self.vehicle.drive(80)
        self.assertEqual(self.vehicle.fuel, 0)
    
    def test_refuel_not_much_fuel(self):
        self.vehicle.fuel = 49
        self.vehicle.refuel(51)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
    
    def test_refuel_much_fuel(self):
        with self.assertRaises(Exception) as ctx:
            self.vehicle.refuel(self.vehicle.capacity)
        self.assertEqual(ctx.exception.__str__(), "Too much fuel")
    
    
    def test_str(self):
        self.assertEqual(str(self.vehicle), "The vehicle has 101 horse power with 100 fuel left and 1.25 fuel consumption")

if __name__ == "__main__":
    main()