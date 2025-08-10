from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []
    
    def add(self, product: Product):
        self.products.append(product)
    
    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product
    
    def remove(self, product_name: str):
        for idx, product in enumerate(self.products):
            if product.name == product_name:
                self.products.pop(idx)
                return
    
    def __repr__(self) -> str:
        return "\n".join(f"{product.name}: {product.quantity}" for product in self.products)


