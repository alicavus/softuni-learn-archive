from project.second_hand_car import SecondHandCar
from unittest import main, TestCase

class TestSecondHandCarClass(TestCase):
    def setUp(self):
        self.car = SecondHandCar("Moskvitch", "Russian Car", 321, 500.0)
    
    def test_constructor_data(self):
        self.assertEqual("Moskvitch", self.car.model)
        self.assertEqual("Russian Car", self.car.car_type)
        self.assertEqual(321, self.car.mileage)
        self.assertEqual(500.0, self.car.price)
        self.assertEqual([], self.car.repairs)
        self.assertIsInstance(self.car.model, str)
        self.assertIsInstance(self.car.car_type, str)
        self.assertIsInstance(self.car.mileage, int)
        self.assertIsInstance(self.car.price, float)
        self.assertIsInstance(self.car.repairs, list)
    
    def test_price_setter_value_less_than_or_equal_to_one(self):
        for price in -4.0, 0.0, 1.0:
            with self.assertRaises(ValueError) as ctx:
                self.car.price = price
            self.assertEqual('Price should be greater than 1.0!', ctx.exception.args[0])
    
    def test_price_setter_value_greather_than_to_one(self):
        for price in 1.99, 99.01, 590.0, 1000.01:
            self.car.price = price
            self.assertEqual(price, self.car.price)
    
    def test_mileage_setter_value_less_than_or_equal_to_one_hundred(self):
        for mileage in -8, 0, 9, 53, 99, 100:
            with self.assertRaises(ValueError) as ctx:
                self.car.mileage = mileage
            self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', ctx.exception.args[0])
    
    def test_mileage_setter_value_greater_than_one_hundred(self):
        for mileage in 101, 342, 543, 1_000, 1_234:
            self.car.mileage = mileage
            self.assertEqual(mileage, self.car.mileage)
    
    def test_set_promotional_price_increase_or_same_price(self):
        for price in (p + self.car.price for p in [0.0, 0.01, 4, 56.9]):
            with self.assertRaises(ValueError) as ctx:
                self.car.set_promotional_price(price)
            self.assertEqual('You are supposed to decrease the price!', ctx.exception.args[0])
    
    def test_set_promotional_price_decrease_price(self):
        car_price = self.car.price
        for price in (car_price - p for p in [0.01, 5, 40, car_price - 1.01]):
            result = self.car.set_promotional_price(price)
            expected = 'The promotional price has been successfully set.'
            self.assertEqual(expected, result)
    
    def test_need_repair_price_for_repair_higher_than_half_price(self):
        price = self.car.price / 2
        for repair_price in price+77.0, price+0.01, price+45.0, price+3:
            result = self.car.need_repair(repair_price, "Repair Description")
            self.assertEqual('Repair is impossible!', result)
            self.assertNotIn("Repair Description", self.car.repairs)
    
    def test_need_repair_price_for_repair_lower_than_or_equal_to_half_price(self):
        for repair in range(1, 10):
            price = self.car.price/2
            result = self.car.need_repair(price, f"Repair Description {repair}")
            self.assertEqual('Price has been increased due to repair charges.', result)
            self.assertEqual(price * 3, self.car.price)
            self.assertIn(f"Repair Description {repair}", self.car.repairs)
    
    def test___gt__car_type_mismatch(self):
        car = SecondHandCar("Lada", "West Car", 123, 123.0)
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.car > car)
    
    def test___gt__car_types_are_same(self):
        car_price = self.car.price
        for price in car_price, car_price + 0.01, car_price + 2, car_price + 100:
            self.assertFalse(self.car > SecondHandCar(f"Model {price}", "Russian Car", 123, price))
        for price in car_price - 0.01, car_price -  3, car_price - 12.3, car_price - 40:
            self.assertTrue(self.car > SecondHandCar(f"Model {price}", "Russian Car", 123, price))
    
    def test__str__(self):
        for repairs in range(10):
            self.car.repairs = [f"Repair Description {n}" for n in range(repairs)]
            self.assertEqual(f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}""", str(self.car))
    


if __name__ == "__main__":
    main()