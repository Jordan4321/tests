import unittest
from parameterized import parameterized
from calc.calc_app import Calc


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    @parameterized.expand([
        ('negative', -3, -2, -5),
        ('mixed', -3, 2, -1),
        ('mixed', 3, -2, 1),
        ('positive', 3, 2, 5)
    ])
    def test_add(self, name, x, y, result):
        self.assertEqual(self.calc.add(x, y), result)
