from oop.mvc.model import OrderModel
from oop.mvc.view import OrderView

class Order:
    model = OrderModel
    view = OrderView

    def __init__(self, order_id):
        self.order_id = order_id

    def post(self):
        order_model = self.model().create(self.order_id)
        return self.view().render(order_model)

    def get(self):
        return self.view().render('')

if __name__ == '__main__':
    order = Order(100)
    print(order.get())
    print(order.post())