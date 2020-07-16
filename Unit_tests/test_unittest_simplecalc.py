from simple_calc import SimpleCalc
import unittest

class Calctest(unittest.TestCase):  # Create class that contains your tests and which inherits all methods from TestCase class
    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(3, 9), 12)
        self.assertEqual(self.calc.add(-5, 20), 15)
        self.assertEqual(self.calc.add(3, -9), -6)
        self.assertIsNotNone(self.calc.add(0, 0))

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 2), 8)
        self.assertEqual(self.calc.subtract(9, 15), -6)
        self.assertEqual(self.calc.subtract(9, -15), 24)
        self.assertEqual(self.calc.subtract(-30, -7), -23)
        self.assertIsNotNone(self.calc.subtract(0, 0))

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(20, 5), 100)
        self.assertEqual(self.calc.multiply(4, 30), 120)
        self.assertEqual(self.calc.multiply(0, 30), 0)
        self.assertIsNotNone(self.calc.multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(25, 5), 5)
        self.assertEqual(self.calc.divide(75, 5), 15)
        self.assertEqual(self.calc.divide(28, 1), 28)
        self.assertIsNotNone(self.calc.divide(0, 1), 0)
