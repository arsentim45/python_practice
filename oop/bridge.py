class Requests:
    def __init__(self, api):
        self.api = api

    def get_product(self):
        self.api.get_data()

class ApiV1:

    def get_product(self):
        self.get('www.visitItdot.com')

class ApiV2:
    def get_product(self):
        self.get('www.visit_it.com')