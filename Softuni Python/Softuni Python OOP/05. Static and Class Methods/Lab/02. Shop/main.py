from collections import defaultdict
class Shop:
    SMALL_SHOP_CAPACITY: int = 10
    def __init__(self, name: str, shop_type: str, capacity: int):
        self.name: str = name
        self.type: str = shop_type
        self.capacity: int = capacity
        self.items: dict[str, int] = {}
    
    @classmethod
    def small_shop(cls, name: str, shop_type: str):
        return cls(name, shop_type, cls.SMALL_SHOP_CAPACITY)
    
    @property
    def count_items(self) -> int:
        return sum([value for value in self.items.values()]) if self.items else 0
    
    def add_item(self, item_name: str) -> str:
        if self.capacity > self.count_items:
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"
    
    def remove_item(self, item_name: str, amount: int) -> str:
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"
    
    def __repr__(self) -> str:
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
