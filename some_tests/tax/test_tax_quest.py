import unittest
from tax_quest import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_type_age_raise_error(self):
        self.assertRaises(TypeError, calc_tax, 100, 0.23, '20')

    def test_value_age_raise_error(self):
        self.assertRaises(ValueError, calc_tax, 100, 0.23, -20)

    def test_calc_tax_age(self):
        self.assertEqual(calc_tax(20, 0.10, 17), 2)
        self.assertEqual(calc_tax(20, 0.10, 64), 2)
        self.assertEqual(calc_tax(20, 0.10, 66), 2)

    def test_calc_tax_age_not_equal1(self):  # wrong equal
        self.assertEqual(4, calc_tax(20, 0.10, 17))

    def test_calc_tax_age_not_equal2_negative(self):  # negative number
        self.assertEqual(-9, calc_tax(20, 0.10, 64))

    def test_calc_tax_age_not_equal3_str(self):  # use str - fail
        self.assertEqual('9', calc_tax(20, 0.10, 64))

    def test_calc_tax_age_negative_error(self):  # age can't be negative
        self.assertEqual(2, calc_tax(20, 0.10, -66))

    def test_calc_tax_age_type_float(self):  # we use int - error
        self.assertEqual(2, calc_tax(20, 0.10, 6.6))

    def test_calc_tax_age_type_str(self):  # we use str - error
        self.assertEqual(2, calc_tax(20, 0.10, '17'))


