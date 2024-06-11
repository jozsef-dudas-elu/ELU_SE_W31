import unittest
from shopping_cart import calculate_total

class TestShoppingCart(unittest.TestCase):

    def test_calculate_with_empty_cart(self):
        """Test calculation with an empty cart"""
        cart = []
        result = calculate_total(cart)
        self.assertEqual(result, 0.0)  # The total for an empty cart should be 0.0

    def test_calculate_with_one_item(self):
        """Test calculation with a single item in the cart"""
        cart = [{'name': 'Beer A', 'price': 4.99}]
        result = calculate_total(cart)
        self.assertEqual(result, 4.99)  # The total should be the price of the single item

    def test_calculate_with_multiple_items(self):
        """Test calculation with multiple items in the cart"""
        cart = [
            {'name': 'Beer A', 'price': 4.99},
            {'name': 'Beer B', 'price': 3.99},
            {'name': 'Beer C', 'price': 5.49}
        ]
        result = calculate_total(cart)
        self.assertEqual(result, 14.47)  # The total should be the sum of all item prices

    def test_calculate_with_negative_prices(self):
        """Test calculation with items having negative prices"""
        cart = [
            {'name': 'Beer A', 'price': 4.99},
            {'name': 'Discount', 'price': -1.00},
        ]
        result = calculate_total(cart)
        self.assertEqual(result, 3.99)  # The total should be the sum of all items, correctly handling negative prices
