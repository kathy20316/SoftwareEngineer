import unittest
from order_model import Order  # Replace 'your_module' with the actual module name

class TestOrderMethods(unittest.TestCase):
    def setUp(self):
        # Reset orders before each test
        Order.orders = []
        self.order1 = Order(1, "Alice", 100)
        self.order2 = Order(2, "Bob", 200)

    def test_get_all_orders(self):
        orders = Order.get_all_orders()
        self.assertEqual(len(orders), 2)
        self.assertEqual(orders[0].customer, "Alice")
        self.assertEqual(orders[1].customer, "Bob")

    def test_empty_orders(self):
        Order.orders = []  # Reset to simulate no orders
        orders = Order.get_all_orders()
        self.assertEqual(len(orders), 0)

if __name__ == "__main__":
    unittest.main()
