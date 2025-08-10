class Trainer:
    id: int = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.__class__.id
        self.__class__.id += 1
    
    @classmethod    
    def get_next_id(self) -> int:
        return Trainer.id
    
    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
    
