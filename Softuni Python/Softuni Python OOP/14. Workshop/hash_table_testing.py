from unittest import main, TestCase

from hash_table import HashTable

class TestHashTable(TestCase):
    def setUp(self):
        self.hash_table = HashTable(capacity=4)
        self.hash_table["hello"] = "Hello World!"
        self.hash_table[False] = True
        self.hash_table[98.6] = 37

    def test_should_create_hash_table(self):
        self.assertIsNotNone(self.hash_table)

    def test_should_report_len_of_empty_table(self):
        self.assertEqual(0, len(HashTable(100)))

    def test_should_create_empty_pair_slots(self):
        hash_table = HashTable(4)
        expected = [None, None, None, None]
        actual = hash_table._array
        self.assertEqual(expected, actual)

    def test_should_inset_key_value_pairs(self):
        self.assertIn(("hello", "Hello World!"), self.hash_table.array)
        self.assertIn((False, True), self.hash_table.array)
        self.assertIn((98.6, 37), self.hash_table.array)
        self.assertEqual(3, len(self.hash_table))

    def test_should_not_shrink_table_on_del(self):
        del self.hash_table["hello"]
        actual = self.hash_table._array
        self.assertEqual(4, len(actual))

    def test_should_find_value_by_key(self):
        self.assertEqual("Hello World!", self.hash_table["hello"])
        self.assertEqual(37, self.hash_table[98.6])
        self.assertEqual(True, self.hash_table[False])

    def test_should_raise_error_on_missing_key(self):
        with self.assertRaises(KeyError) as e:
            test = self.hash_table["missing"]
        self.assertEqual("missing", e.exception.args[0]) # str(e.exception)

    def test_should_find_key(self):
        self.assertIn("hello", self.hash_table)
        self.assertIn(False, self.hash_table)
        self.assertIn(98.6, self.hash_table)



if __name__ == "__main__":
    main()