from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore

class FactoryManager:
    VALID_PRODUCTS = {
        "Chair": Chair,
        "HobbyHorse": HobbyHorse
    }
    VALID_STORES = {
        'FurnitureStore': FurnitureStore,
        'ToyStore': ToyStore
    }
    def __init__(self, name: str):
        self.name: str = name
        self.income: float = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []
    
    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.VALID_PRODUCTS:
            raise Exception("Invalid product type!")
        product: BaseProduct = self.VALID_PRODUCTS[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."
    
    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.VALID_STORES:
            raise Exception(f"{store_type} is an invalid type of store!")
        self.stores.append(self.VALID_STORES[store_type](name, location))

        return f"A new {store_type} was successfully registered."
    
    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {self.name} has no capacity for this purchase."
        count = 0
        for product in products:
            if product.sub_type == str(store):
                self.income += product.price
                store.capacity -= 1
                store.products.append(product)
                count += 1
                self.products.remove(product)
        
        if count:
            return f"Store {store.name} successfully purchased {count} items."
        return "Products do not match in type. Nothing sold."
    
    def unregister_store(self, store_name: str):
        store = next((store for store in self.stores if store.name == store_name), None)
        if not store:
            raise Exception("No such store!")
        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."
        return f"Successfully unregistered store {store_name}, location: {store.location}."
    
    def discount_products(self, product_model: str):
        count = 0
        for product in self.products:
            if product.model == product_model:
                product.discount()
                count += 1
        return f"Discount applied to {count} products with model: {product_model}"
    
    def request_store_stats(self, store_name: str):
        store: BaseStore = next((store for store in self.stores if store.name == store_name), None)
        if not store:
            return "There is no store registered under this name!"
        return store.store_stats()
    
    def statistics(self):
        result = [f"Factory: {self.name}",
                  f"Income: {self.income:.2f}",
                  "***Products Statistics***"
                  ]
        total_price = 0
        products = {}
        for product in self.products:
            total_price += product.price
            if product.model not in products:
                products[product.model] = 0
            products[product.model] += 1
        result.append(f"Unsold Products: {len(self.products)}. Total net price: {total_price:.2f}")
        result.extend([
            f"{product_model}: {count}" for product_model, count in sorted(products.items(), key=lambda p: p[0])
        ])

        result += [f"***Partner Stores: {len(self.stores)}***"]
        result.extend([
            store.name for store in sorted(self.stores, key=lambda s: s.name)
        ])
        return "\n".join(result)


