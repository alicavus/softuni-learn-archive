from project.legendary_item import LegendaryItem
from unittest import main, TestCase

class TestLegendaryItemClass(TestCase):
    def setUp(self):
        self.item = LegendaryItem("Legend-01", 88, 55, 750)
    
    def test_initialisation_data(self):
        self.assertEqual("Legend-01", self.item.identifier)
        self.assertEqual(88, self.item.power)
        self.assertEqual(55, self.item.durability)
        self.assertEqual(750, self.item.price)

    def test_identifier_setter_contains_other_charcters_should_rise_error(self):
        for identifier in "", "&koppa", "test$lol", "ident_des", "Lol1?09":
            with self.assertRaises(ValueError) as ve:
                LegendaryItem(identifier, 88, 55, 1000)
            self.assertEqual("Identifier can only contain letters, digits, or hyphens!", ve.exception.args[0])
    
    def test_identifier_setter_len_not_sufficient_should_rise_error(self):
        for identifier in "ppa", "123", "X", "3", "Lo":
            with self.assertRaises(ValueError) as ve:
                LegendaryItem(identifier, 88, 55, 1000)
            self.assertEqual("Identifier must be at least 4 characters long!", ve.exception.args[0])
    
    def test_identifier_setter_should_set_when_no_error(self):
        for identifier in "ppax", "123E", "Xxxx-87", "3ABCD", "Lo-786":
            self.item.identifier = identifier
            self.assertEqual(identifier, self.item.identifier)
    
    def test_power_setter_negative_value_should_rise_error(self):
        for power in -123, -1, -67:
            with self.assertRaises(ValueError) as ve:
                LegendaryItem("identifier", power, 55, 1000)
            self.assertEqual("Power must be a non-negative integer!", ve.exception.args[0])
    
    def test_power_setter_non_negative_value_should_set_new_value(self):
        for power in 0, 1, 22, 55:
            self.item.power = power
            self.assertEqual(power, self.item.power)
    
    def test_durability_setter_non_valid_values_should_rise_error(self):
        for durability in -8, 0, 101, 123:
            with self.assertRaises(ValueError) as ve:
                LegendaryItem("identifier", 55, durability, 1000)
            self.assertEqual("Durability must be between 1 and 100 inclusive!", ve.exception.args[0])
    
    def test_durability_setter_valid_values_should_set_them(self):
        for durability in 1, 11, 34, 90, 100:
            self.item.durability = durability
            self.assertEqual(durability, self.item.durability)
    
    def test_price_setter_non_multiple_of_ten_should_rise_error(self):
        for price in 0, 33, 45, 654, 1111:
            with self.assertRaises(ValueError) as ve:
                LegendaryItem("identifier", 55, 99, price)
            self.assertEqual("Price must be a multiple of 10 and not 0!", ve.exception.args[0])
    def test_price_setter_multiple_of_ten_should_set_value(self):
        for price in 30, 450, 6540, 111100:
            self.item.price = price
            self.assertEqual(price, self.item.price)

    def test_is_precious(self):
        for power in 0, 11, 32, 44, 49:
            item = LegendaryItem("identifier", power, 99, 1000)
            self.assertFalse(item.is_precious)
        
        for power in 50, 51, 52, 101, 467:
            item = LegendaryItem("identifier", power, 99, 1000)
            self.assertTrue(item.is_precious)
    
    def test_enhance(self):
        power = 15
        durability = 45
        price = 10
        item = LegendaryItem("item01", power, durability, price)

        for i in range(1, 101):
            res = item.enhance()
            power *= 2
            price += 10
            durability = min(durability + 10, 100)
            self.assertIsNone(res)
            self.assertEqual(power, item.power)
            self.assertEqual(price, item.price)
            self.assertEqual(durability, item.durability)
    
    def test_evaluate_non_precious_should_return_non_eligible(self):
        for power in 0, 11, 32, 44, 49:
            item = LegendaryItem("identifier", power, 99, 1000)
            self.assertEqual("Item not eligible.", item.evaluate(0))
    
    def test_evaluate_less_durable_should_return_non_eligible(self):
        for durability in 1, 11, 34, 90:
            self.item.durability = durability
            for k in range(1, 11):
                self.assertEqual("Item not eligible.", self.item.evaluate(durability + k))
    
    def test_evaluate_eligible(self):
        for durability in 1, 11, 34, 90:
            self.item.durability = durability
            for k in range(11):
                self.assertEqual("Legend-01 is eligible.", self.item.evaluate(durability - k))

        
        


if __name__ == "__main__":
    main()

