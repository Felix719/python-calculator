import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        

    # Add the following test methods to the TestCalculator class:
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)  
        self.assertEqual(self.calc.add(-1, 1), 0)  

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)  
        self.assertEqual(self.calc.subtract(2, 5), -3)  

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)  
        self.assertEqual(self.calc.multiply(-2, 5), -10)  

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)  
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)  

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)  
        self.assertEqual(self.calc.modulo(7, 5), 2)  
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(10, 0)  

if __name__ == '__main__':
    unittest.main()