class Category:
    def __init__(self, category_id: int, name: str):
        self.id: int = category_id
        self.name: str = name
    
    def edit(self, new_name: str):
        self.name = new_name
        return self
    
    def __repr__(self) -> str:
        return f"Category {self.id}: {self.name}"
