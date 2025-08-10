from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient

from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter

class SphereRestaurantApp:
    VALID_WAITERS = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter
    }
    VALID_CLIENTS = {
        "RegularClient": RegularClient,
        "VIPClient": VIPClient
    }
    def __init__(self):
        self.waiters: list[BaseWaiter] = []
        self.clients: list[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int) -> str:
        if waiter_type not in self.VALID_WAITERS:
            return f"{waiter_type} is not a recognized waiter type."

        if self.get_item(self.waiters, "name", waiter_name) is not None:
            return f"{waiter_name} is already on the staff."

        self.waiters.append(self.VALID_WAITERS[waiter_type](waiter_name, hours_worked))

        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str) -> str:
        if client_type not in self.VALID_CLIENTS:
            return f"{client_type} is not a recognized client type."

        if self.get_item(self.clients, "name", client_name) is not None:
            return f"{client_name} is already a client."

        self.clients.append(self.VALID_CLIENTS[client_type](client_name))

        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str) -> str:
        waiter: BaseWaiter = self.get_item(self.waiters, "name", waiter_name)

        if waiter is None:
            return f"No waiter found with the name {waiter_name}."

        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float) -> str:
        client: BaseClient = self.get_item(self.clients, "name", client_name)

        if client is None:
            return f"{client_name} is not a registered client."

        points_earned = client.earning_points(order_amount)

        return f"{client_name} earned {points_earned} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client: BaseClient = self.get_item(self.clients, "name", client_name)

        if client is None:
            return f"{client_name} cannot get a discount because this client is not admitted!"
        discount_percentage, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

    def generate_report(self):
        waiters = {}
        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)

        result = [
            "$$ Monthly Report $$",
            f"Total Earnings: ${total_earnings:.2f}",
            f"Total Clients Unused Points: {sum(client.points for client in self.clients)}",
            f"Total Clients Count: {len(self.clients)}",
            "** Waiter Details **"
        ]

        result.extend([
            str(waiter) for waiter in sorted(self.waiters, key=lambda w: -w.calculate_earnings())
        ])

        return "\n".join(result)

    # helpers
    @staticmethod
    def get_item(collection, attribute_name = None, attribute_value = None):
        generator = (item for item in collection if getattr(item, attribute_name) == attribute_value) if attribute_name is not None else (item for item in collection)

        return next(generator, None)

    @staticmethod
    def get_items(collection, attribute_name = None, attribute_value = None):
        if attribute_name is not None:
            return (item for item in collection if getattr(item, attribute_name) == attribute_value)
        return (item for item in collection)

