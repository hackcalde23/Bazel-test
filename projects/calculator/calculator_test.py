import unittest
from projects.calculator.calculator import calculator

class TestSum(unittest.TestCase):
    def test_sum(self):
        calc = calculator()
        self.assertEqual(calc.add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()