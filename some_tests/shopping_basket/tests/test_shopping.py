import unittest
from shopping.basket import ShoppingBasket


class TestShoppingBasketWithNoProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO} setting up basket without any product')
        cls.basket = ShoppingBasket()

    def test_size_of_basket_should_be_empty(self):
        self.assertEqual(len(self.basket), 0)

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 0)

    def test_total_amount_should_be_zero(self):
        self.assertEqual(self.basket.total(), 0)


class TestShoppingBasketWithOneProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO} setting up basket with one product')
        cls.basket = ShoppingBasket().add_product('milk', 3.0)

    def test_getting_product(self):
        self.assertEqual('milk', self.basket.get_product(0).name)

    def test_size_of_basket_should_be_one(self):
        self.assertEqual(len(self.basket), 1)

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 1)

    def test_total_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 3.63)


class TestShoppingBasketWithTwoProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO} setting up basket with two product')
        cls.basket = ShoppingBasket()\
            .add_product('milk', 3.0)\
            .add_product('water', 2.0)

    def test_getting_two_product(self):
        self.assertEqual(self.basket.get_product(0).name, 'milk')
        self.assertEqual(self.basket.get_product(1).name, 'water')

    def test_size_of_basket_should_be_Two(self):
        self.assertEqual(len(self.basket), 2)

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 2)

    def test_total_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 6.05)

    def test_order_of_products(self):
        self.assertEqual(self.basket.get_product(0).name, 'milk')
        self.assertEqual(self.basket.get_product(1).name, 'water')
        self.assertEqual(self.basket.get_product(0).price, 3.0)
        self.assertEqual(self.basket.get_product(1).price, 2.0)
