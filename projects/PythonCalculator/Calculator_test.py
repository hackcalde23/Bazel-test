import unittest
from projects.PythonCalculator.Calculator import Calculator

class TestSum(unittest.TestCase):
    def test_sum(self):
        calc = Calculator()
        self.assertEqual(calc.add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()