from project.clients import BaseClient, BusinessClient, RegularClient
from project.plants import BasePlant, Flower, LeafPlant
from collections import  defaultdict

class FlowerShopManager:
    def __init__(self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str) -> str:
        if plant_type not in ("Flower", "LeafPlant"):
            raise ValueError("Unknown plant type!")
        p = Flower if plant_type == "Flower" else LeafPlant
        self.plants.append(p(plant_name, plant_price, plant_water_needed, plant_extra_data))
        return f"{plant_name} is added to the shop as {plant_type}."

    @staticmethod
    def get_items(collection, attribute, value):
        return (c for c in collection if getattr(c, attribute) == value)

    def add_client(self, client_type: str, client_name: str, client_phone_number: str) -> str:
        if client_type not in ("RegularClient", "BusinessClient"):
            raise ValueError("Unknown client type!")
        if next(self.get_items(self.clients, "phone_number", client_phone_number), None) is not None:
            raise ValueError("This phone number has been used!")
        c = BusinessClient if client_type == "BusinessClient" else RegularClient
        self.clients.append(c(client_name, client_phone_number))
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next(self.get_items(self.clients, "phone_number", client_phone_number), None)
        if client is None:
            raise ValueError("Client not found!")
        plants = list(self.get_items(self.plants, "name", plant_name))
        if not plants:
            raise ValueError("Plants not found!")
        if len(plants) < plant_quantity:
            return "Not enough plant quantity."
        order_amount = 0
        for _ in range(plant_quantity):
            plant = plants.pop()
            self.plants.remove(plant)
            current_order_amount = plant.price * (1 - client.discount * 0.01)
            self.income += current_order_amount
            order_amount += current_order_amount

        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name: str):
        plant = next(self.get_items(self.plants, "name", plant_name), None)
        if plant is None:
            return  "No such plant name."
        self.plants.remove(plant)
        return  f"Removed {plant.plant_details()}"

    def remove_clients(self):
        cnt = 0
        for client in list(self.get_items(self.clients, "total_orders", 0)):
            cnt += 1
            self.clients.remove(client)
        return f"{cnt} client/s removed."

    def shop_report(self):
        plants = defaultdict(int)

        unsold_plants_count = len(self.plants)
        for plant in self.plants:
            plants[plant.name] += 1

        total_orders = 0
        for client in self.clients:
            total_orders += client.total_orders

        result = ["~Flower Shop Report~", f"Income: {self.income:.2f}", f"Count of orders: {total_orders}", f"~~Unsold plants: {unsold_plants_count}~~"]
        sorted_plants = sorted(plants.items(), key=lambda item: (-item[1], item[0]))
        sorted_clients = sorted(self.clients, key=lambda item: (-item.total_orders, item.phone_number))
        result.extend([f"{plant_name}: {count}" for plant_name, count in sorted_plants])
        result.append(f"~~Clients number: {len(self.clients)}~~")
        result.extend([client.client_details() for client in sorted_clients])

        return "\n".join(result)




