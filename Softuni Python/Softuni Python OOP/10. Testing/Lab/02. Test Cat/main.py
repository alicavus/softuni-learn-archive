class Cat:
    def __init__(self, name):
      self.name = name
      self.fed = False
      self.sleepy = False
      self.size = 0
      
    def eat(self):
       if self.fed:
          raise Exception('Already fed.')
       
       self.fed = True
       self.sleepy = True
       self.size += 1
       
    def sleep(self):
       if not self.fed:
          raise Exception('Cannot sleep while hungry')
       
       self.sleepy = False

import unittest

class CatTests(unittest.TestCase):
    def setUp(self):
       self.cat = Cat(name="Tom")
    
    def test_size_increased_after_eat(self):
       size_before = self.cat.size
       self.cat.eat()
       size_after = self.cat.size
       self.assertEqual(size_after - 1, size_before)
    
    def test_fed_after_eat(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
    
    def test_cannot_eat_if_fed_raises_error(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ctx:
            self.cat.eat()
        self.assertEqual(ctx.exception.__str__(), 'Already fed.')
    
    def test_cannot_fall_asleep_not_fed_raises_error(self):
        with self.assertRaises(Exception) as ctx:
            self.cat.sleep()
        self.assertEqual(ctx.exception.__str__(), 'Cannot sleep while hungry')
    
    def test_not_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    

if __name__ == "__main__":
   unittest.main()