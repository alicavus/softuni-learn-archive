from project.clients.base_client import BaseClient

class RegularClient(BaseClient):
    def __init__(self, name, phone_number):
        super().__init__(name, phone_number)

    def update_discount(self):
        if self.total_orders >= 1:
            self.discount = 5.0
    