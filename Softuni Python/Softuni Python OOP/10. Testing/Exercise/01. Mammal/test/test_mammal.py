from project.mammal import Mammal
import unittest

class MammalTest(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Ines Ivanova", "Cow", "Mooo")
    
    def test_constructor_data(self):
        self.assertEqual(self.mammal.name, "Ines Ivanova")
        self.assertEqual(self.mammal.type, "Cow")
        self.assertEqual(self.mammal.sound, "Mooo")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")
    
    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Ines Ivanova makes Mooo")
    
    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")
    
    def test_info(self):
        self.assertEqual(self.mammal.info(), "Ines Ivanova is of type Cow")

if __name__ == "__main__":
    unittest.main()
