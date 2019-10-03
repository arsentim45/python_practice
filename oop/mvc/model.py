from random import randint
from datetime import datetime
storage = {}

class OrderModel:

    def create(self, order_id):
        global storage
        storage[order_id] = 'created on ' + str(datetime.now()) + ' ' + str(randint(1, 10)) + ' order copies'
        return storage[order_id]