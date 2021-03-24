import unittest

class Calculator():
    def add_num(self, a, b):
        c = a + b
        return c

class TestNumber(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 2, 3)
        self.assertEqual(2 + 2, 4)
 
    def testMultiply(self):
       self.assertEqual(1 * 1, 1)
       self.assertEqual(1 * 2, 2)
       self.assertEqual(2 * 4, 8)
    
    def test_hello_world(self):
        myCal = Calculator();
        self.assertEqual(myCal.add_num(1,2), 3)
 
if __name__ == '__main__':
   unittest.main()