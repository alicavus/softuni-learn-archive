class Equipment:
    id: int = 1
    def __init__(self, name: str):
        self.name: str = name
        self.id = self.__class__.id
        self.__class__.id += 1
    
    @classmethod    
    def get_next_id(self) -> int:
        return Equipment.id
    
    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"
    