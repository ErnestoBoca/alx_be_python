import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2,3), 5)
        self.assertEqual(self.calc.add(-2,3), 1)
        self.assertEqual(self.calc.add(2,-3), -1)
        self.assertEqual(self.calc.add(-1,-3), -4)
        self.assertEqual(self.calc.add(-1,1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2,3), -1)
        self.assertEqual(self.calc.subtract(-2,3), -5)
        self.assertEqual(self.calc.subtract(2,-3), 5)
        self.assertEqual(self.calc.subtract(1,1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,3), 6)
        self.assertEqual(self.calc.multiply(2,0), 0)
        self.assertEqual(self.calc.multiply(2,-3), -6)
        self.assertEqual(self.calc.multiply(-3,-3), 9)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        self.assertEqual(self.calc.divide(6, 0), None)

    
