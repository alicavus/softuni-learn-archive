from project.furniture import Furniture
from unittest import main, TestCase

class TestFurniture(TestCase):
    def setUp(self):
        self.furniture1 = Furniture("Furniture Module 1", 75.5, (5, 7, 5))
        self.furniture2 = Furniture("Furniture Module 2", 112.0, (15, 1, 1), False)
        self.furniture3 = Furniture("Furniture Module 3", 87.0, (1, 1, 1), False, 32.0)
    
    def test_constructor(self):
        self.assertEqual("Furniture Module 1", self.furniture1._model)
        self.assertEqual("Furniture Module 2", self.furniture2._model)
        self.assertEqual("Furniture Module 3", self.furniture3._model)

        self.assertEqual(75.5, self.furniture1._price)
        self.assertEqual(112.0, self.furniture2._price)
        self.assertEqual(87.0, self.furniture3._price)

        self.assertEqual((5, 7, 5), self.furniture1._dimensions)
        self.assertEqual((15, 1, 1), self.furniture2._dimensions)
        self.assertEqual((1, 1, 1), self.furniture3._dimensions)

        self.assertTrue(self.furniture1.in_stock)
        self.assertFalse(self.furniture2.in_stock)
        self.assertFalse(self.furniture3.in_stock)

        self.assertIsNone(self.furniture1._weight)
        self.assertIsNone(self.furniture2._weight)
        self.assertEqual(32.0, self.furniture3._weight)

    def test_property(self):
        self.assertEqual(self.furniture1.model, self.furniture1._model)
        self.assertEqual(self.furniture1.price, self.furniture1._price)
        self.assertEqual(self.furniture1.dimensions, self.furniture1._dimensions)
        self.assertEqual(self.furniture1.weight, self.furniture1._weight)

        self.assertEqual(self.furniture2.model, self.furniture2._model)
        self.assertEqual(self.furniture2.price, self.furniture2._price)
        self.assertEqual(self.furniture2.dimensions, self.furniture2._dimensions)
        self.assertEqual(self.furniture2.weight, self.furniture2._weight)

        self.assertEqual(self.furniture3.model, self.furniture3._model)
        self.assertEqual(self.furniture3.price, self.furniture3._price)
        self.assertEqual(self.furniture3.dimensions, self.furniture3._dimensions)
        self.assertEqual(self.furniture3.weight, self.furniture3._weight)
    
    def test_model_setter_invalid(self):
        expected = "Model must be a non-empty string with a maximum length of 50 characters."

        with self.assertRaises(ValueError) as ctx:
            self.furniture1.model = "       "
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture1.model = "   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  "
        self.assertEqual(expected, ctx.exception.__str__())
        
        with self.assertRaises(ValueError) as ctx:
            self.furniture2.model = "       "
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture2.model = "   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  "
        self.assertEqual(expected, ctx.exception.__str__())
        
        with self.assertRaises(ValueError) as ctx:
            self.furniture3.model = "       "
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture3.model = "   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  "
        self.assertEqual(expected, ctx.exception.__str__())
    
    def test_model_setter_valid(self):
        self.furniture1.model = "Furnit Model New"
        self.assertEqual("Furnit Model New", self.furniture1._model)

        self.furniture2.model = "Furnit Model New"
        self.assertEqual("Furnit Model New", self.furniture2._model)
    
        self.furniture3.model = "Furnit Model New"
        self.assertEqual("Furnit Model New", self.furniture3._model)
    
    def test_price_setter_price_negative(self):
        expected = "Price must be a non-negative number."
        with self.assertRaises(ValueError) as ctx:
            self.furniture1.price = -4
        self.assertEqual(expected, ctx.exception.__str__())

        with self.assertRaises(ValueError) as ctx:
            self.furniture2.price = -4
        self.assertEqual(expected, ctx.exception.__str__())

        with self.assertRaises(ValueError) as ctx:
            self.furniture3.price = -4
        self.assertEqual(expected, ctx.exception.__str__())
    
    def test_price_setter_price_non_negative(self):
        self.furniture1.price = 4.5
        self.assertEqual(4.5, self.furniture1._price)
        self.furniture2.price = 4.5
        self.assertEqual(4.5, self.furniture2._price)
        self.furniture3.price = 4.5
        self.assertEqual(4.5, self.furniture3._price)
    
    def test_dimensions_setter_not_tree_params(self):
        expected = "Dimensions tuple must contain 3 integers."
        with self.assertRaises(ValueError) as ctx:
            self.furniture1.dimensions = (5, 7)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture1.dimensions = (5, 7, 11, 4)
        self.assertEqual(expected, ctx.exception.__str__())

        with self.assertRaises(ValueError) as ctx:
            self.furniture2.dimensions = (5, 7)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture2.dimensions = (5, 7, 11, 4)
        self.assertEqual(expected, ctx.exception.__str__())

        with self.assertRaises(ValueError) as ctx:
            self.furniture3.dimensions = (5, 7)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture3.dimensions = (5, 7, 11, 4)
        self.assertEqual(expected, ctx.exception.__str__())
    
    def test_dimensions_setter_tree_params_negative_or_zero_param(self):
        expected = "Dimensions tuple must contain integers greater than zero."
        with self.assertRaises(ValueError) as ctx:
            self.furniture1.dimensions = (0, 7, 11)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture1.dimensions = (7, 0, 11)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture1.dimensions = (7, 11, 0)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture1.dimensions = (-1, 7, 11)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture1.dimensions = (7, -1, 11)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture1.dimensions = (7, 11, -1)
        self.assertEqual(expected, ctx.exception.__str__())

        with self.assertRaises(ValueError) as ctx:
            self.furniture2.dimensions = (0, 7, 11)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture2.dimensions = (7, 0, 11)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture2.dimensions = (7, 11, 0)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture2.dimensions = (-1, 7, 11)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture2.dimensions = (7, -1, 11)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture2.dimensions = (7, 11, -1)
        self.assertEqual(expected, ctx.exception.__str__())

        with self.assertRaises(ValueError) as ctx:
            self.furniture3.dimensions = (0, 7, 11)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture3.dimensions = (7, 0, 11)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture3.dimensions = (7, 11, 0)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture3.dimensions = (-1, 7, 11)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture3.dimensions = (7, -1, 11)
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture3.dimensions = (7, 11, -1)
        self.assertEqual(expected, ctx.exception.__str__())
    
    def test_dimensions_setter_tree_params_ok(self):
        self.furniture1.dimensions = (1, 2, 3)
        self.assertEqual((1, 2, 3), self.furniture1._dimensions)
        self.furniture2.dimensions = (1, 2, 3)
        self.assertEqual((1, 2, 3), self.furniture2._dimensions)
        self.furniture3.dimensions = (1, 2, 3)
        self.assertEqual((1, 2, 3), self.furniture3._dimensions)
    
    def test_weight_setter_none_value(self):
        self.furniture1.weight = None
        self.furniture2.weight = None
        self.furniture3.weight = None
        self.assertEqual(None, self.furniture1._weight)
        self.assertEqual(None, self.furniture2._weight)
        self.assertEqual(None, self.furniture3._weight)
        
    def test_weight_setter_non_positive_value(self):
        expected = "Weight must be greater than zero."
        with self.assertRaises(ValueError) as ctx:
            self.furniture1.weight = 0
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture1.weight = -9
        self.assertEqual(expected, ctx.exception.__str__())

        with self.assertRaises(ValueError) as ctx:
            self.furniture2.weight = 0
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture2.weight = -9
        self.assertEqual(expected, ctx.exception.__str__())

        with self.assertRaises(ValueError) as ctx:
            self.furniture3.weight = 0
        self.assertEqual(expected, ctx.exception.__str__())
        with self.assertRaises(ValueError) as ctx:
            self.furniture3.weight = -9
        self.assertEqual(expected, ctx.exception.__str__())
    
    def test_weight_setter_positive_value(self):
        self.furniture1.weight = 12.3
        self.furniture2.weight = 12.3
        self.furniture3.weight = 12.3
        self.assertEqual(12.3, self.furniture1._weight)
        self.assertEqual(12.3, self.furniture2._weight)
        self.assertEqual(12.3, self.furniture3._weight)
    
    def test_get_available_status_available(self):
        self.assertEqual("Model: Furniture Module 1 is currently in stock.", self.furniture1.get_available_status())
        self.assertEqual("Model: Furniture Module 2 is currently unavailable.", self.furniture2.get_available_status())
        self.assertEqual("Model: Furniture Module 3 is currently unavailable.", self.furniture3.get_available_status())
    
    def test_get_specifications(self):
        self.assertEqual("Model: Furniture Module 1 has the following dimensions: 5mm x 7mm x 5mm and weighs: N/A", self.furniture1.get_specifications())
        self.assertEqual("Model: Furniture Module 2 has the following dimensions: 15mm x 1mm x 1mm and weighs: N/A", self.furniture2.get_specifications())
        self.assertEqual("Model: Furniture Module 3 has the following dimensions: 1mm x 1mm x 1mm and weighs: 32.0", self.furniture3.get_specifications())
        


if __name__ == "__main__":
    main()