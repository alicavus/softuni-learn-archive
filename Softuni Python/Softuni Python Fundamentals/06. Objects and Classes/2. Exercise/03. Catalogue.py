class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []
    
    def __repr__(self):
        return "\n".join([f"Items in the {self.name} catalogue:"]+[x for x in sorted(self.products)])
    
    def add_product(self, product_name: str):
        self.products += [product_name]
    
    def get_by_letter(self, first_letter: str):
        return [x for x in self.products if x.startswith(first_letter)]
    
catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
