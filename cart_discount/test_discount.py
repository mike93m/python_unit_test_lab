import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario

    def test_string_in_list(self):
        prices = [10, 'apples', 20]
        with self.assertRaises(TypeError):
            discount(prices)

    def test_discount_with_same_prices(self):
        prices = [5, 5, 5]
        expected_discount = 5
        self.assertEqual(expected_discount, discount(prices))

    def test_discounut_with_two_prices(self):
        prices = [10, 20]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_with_no_prices(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_with_negative_price(self):
        prices = [10, -5, 20]
        expected_discount = -5
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_with_floating_point_prices(self):
        prices = [10.5, 4.2, 20.3]
        expected_discount = 4.2
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_all_negative_prices(self):
        prices = [-10, -20, -5]
        expected_discount = -20
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_list_is_none(self):
        prices = None
        with self.assertRaises(TypeError):
            discount(prices)

    def test_discount_with_dictionary_not_list(self):
        prices = {10, 20, 30}
        with self.assertRaises(TypeError):
            discount(prices)

    def test_discount_with_tuple_not_list(self):
        prices = (10, 20, 30)
        with self.assertRaises(TypeError):
            discount(prices)

    def test_discount_with_big_integer_prices(self):
        prices = [10**6, 10**7, 10**8]
        expected_discount = 10**6
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_with_float_and_integer_prices(self):
        prices = [10, 4.5, 4]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_with_boolean_in_list(self):
        prices = [10, True, 20]
        expected_discount = 1  
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_with_large_list(self):
        prices = list(range(1, 10**6))  
        expected_discount = 1  
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_with_same_value_int_and_float(self):
        prices = [10, 10.0, 10.00]
        expected_discount = 10.00
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_with_long_float_prices(self):
        prices = [10.123456789, 4.987654321, 20.111111111]
        expected_discount = 4.987654321
        self.assertAlmostEqual(expected_discount, discount(prices), places=9) # Places is the number of decimal places to check

if __name__ == '__main__':
    unittest.main()