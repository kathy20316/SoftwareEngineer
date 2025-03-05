class Order:
    orders = []

    def __init__(self, order_id, customer, amount):
        self.order_id = order_id
        self.customer = customer
        self.amount = amount
        Order.orders.append(self)

    @classmethod
    def get_all_orders(cls):
        return cls.orders