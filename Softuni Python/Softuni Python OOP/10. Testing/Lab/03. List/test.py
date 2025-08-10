from List.extended_list import IntegerList
import unittest

class IntegerListTest(unittest.TestCase):
    def setUp(self):
        self.lst = IntegerList(1, 3, 8, 10.0, 'Thomas', {5: []})
        
    def test_init_takes_only_integers(self):
        self.assertNotIn('Thomas', self.lst._IntegerList__data)
        self.assertNotIn(10.0, self.lst._IntegerList__data)
        self.assertNotIn({5: []}, self.lst._IntegerList__data)

        self.assertIn(1, self.lst._IntegerList__data)
        self.assertIn(3, self.lst._IntegerList__data)
        self.assertIn(8, self.lst._IntegerList__data)
    
    def test_get_data(self):
        self.assertEqual(self.lst.get_data(), self.lst._IntegerList__data)
        self.assertEqual(self.lst.get_data(), [1, 3, 8])
    
    def test_add_valid_element(self):
        self.lst.add(13)
        self.assertEqual(self.lst.get_data(), [1, 3, 8, 13])
    
    def test_add_invalid_element(self):
        with self.assertRaises(ValueError) as ctx:
            self.lst.add('Bob')
        self.assertEqual(str(ctx.exception), "Element is not Integer")
    
    def test_remove_invalid_index(self):
        with self.assertRaises(IndexError) as ctx:
            self.lst.remove_index(3)
        self.assertEqual(str(ctx.exception), "Index is out of range")
    
    def test_remove_valid_index(self):
        data = [number for number in self.lst.get_data()]
        idx = 1
        expected_result = data.pop(idx)
        result = self.lst.remove_index(idx)
        self.assertEqual(data, self.lst.get_data())
        self.assertEqual(result, expected_result)
    
    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as ctx:
            self.lst.get(30)
        self.assertEqual(str(ctx.exception), "Index is out of range")
    
    def test_get_valid_index(self):
        result = self.lst.get(1)
        expected_result = 3
        self.assertEqual(result, expected_result)
    
    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError) as ctx:
            self.lst.insert(3, 5)
        self.assertEqual(str(ctx.exception), "Index is out of range")
    
    def test_insert_invalid_value_type(self):
        with self.assertRaises(ValueError) as ctx:
            self.lst.insert(1, '5')
        self.assertEqual(str(ctx.exception), "Element is not Integer")
    
    def test_insert_valid_data(self):
        self.lst.insert(1, 13)
        self.assertEqual(self.lst.get_data(), [1, 13, 3, 8])
    
    def test_get_biggest(self):
        result = self.lst.get_biggest()
        expected_result = 8
        self.assertEqual(result, expected_result)
    
    def test_get_index(self):
        result = self.lst.get_index(8)
        expected_result = 2
        self.assertEqual(result, expected_result)
    

if __name__ == "__main__":
    unittest.main()