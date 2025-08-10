class Subscription:
    id: int = 1
    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date: str = date
        self.customer_id: int = customer_id
        self.trainer_id: int = trainer_id
        self.exercise_id: int = exercise_id
        self.id: int = self.__class__.id
        self.__class__.id += 1
    
    @classmethod    
    def get_next_id(self) -> int:
        return Subscription.id
    
    def __repr__(self) -> str:
        return f"Subscription <{self.id}> on {self.date}"