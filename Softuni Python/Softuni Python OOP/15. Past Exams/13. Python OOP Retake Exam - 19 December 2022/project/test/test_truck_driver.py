from project.truck_driver import TruckDriver
from unittest import main, TestCase

class TestTruckDriverClass(TestCase):
    def setUp(self):
        self.driver = TruckDriver("Truck Driver Name", 1.23)
    
    def test_constructor_data(self):
        self.assertEqual("Truck Driver Name", self.driver.name)
        self.assertEqual(1.23, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
        self.assertIsInstance(self.driver.name, str)
        self.assertIsInstance(self.driver.money_per_mile, float)
        self.assertIsInstance(self.driver.available_cargos, dict)
        self.assertIsInstance(self.driver.earned_money, (int, float))
        self.assertIsInstance(self.driver.miles, int)
    
    def test_earned_money_setter_negative_value_should_raise_error(self):
        for value in -8.0, -1, -0.01:
            with self.assertRaises(ValueError) as ve:
                self.driver.earned_money = value
            self.assertEqual("Truck Driver Name went bankrupt.", ve.exception.args[0])
    
    def test_earned_money_setter_non_negative_value_should_set_new_value(self):
        for value in 0.0, 123.45, 99.99, 1_000:
            self.driver.earned_money = value
            self.assertEqual(value, self.driver.earned_money)
    
    def test_add_cargo_offer_new_cargo_data_should_add_available_cargo_dict(self):
        cargo_data = {f"Cargo Location {number}": miles for number, miles in enumerate(range(11, 121, 7))}
        for cargo in cargo_data:
            result = self.driver.add_cargo_offer(cargo, cargo_data[cargo])
            self.assertIn(cargo, self.driver.available_cargos)
            self.assertEqual(cargo_data[cargo], self.driver.available_cargos.get(cargo))
            self.assertEqual(f"Cargo for {cargo_data[cargo]} to {cargo} was added as an offer.", result)
    
    def test_add_cargo_offer_existing_cargo_location_should_rise_error(self):
        cargo_data = {f"Cargo Location {number}": miles for number, miles in enumerate(range(11, 121, 7))}
        for cargo in cargo_data:
            self.driver.add_cargo_offer(cargo, cargo_data[cargo])
            with self.assertRaises(Exception) as ex:
                self.driver.add_cargo_offer(cargo, 1)
            self.assertEqual("Cargo offer is already added.", ex.exception.args[0])



if __name__ == "__main__":
    main()