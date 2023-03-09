import unittest
from calc.calc_app import Calc


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):

        cases = [
            (-3, -2, -5),
            (-3, 2, -1),
            (3, -2, 1),
            (3, 2, 5)
        ]
        for x, y, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(self.calc.add(x, y), result)
