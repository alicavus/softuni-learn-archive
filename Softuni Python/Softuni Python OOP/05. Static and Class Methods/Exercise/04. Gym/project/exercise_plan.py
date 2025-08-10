class ExercisePlan:
    id: int = 1
    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id: int = trainer_id
        self.equipment_id: int = equipment_id
        self.duration: int = duration
        self.id: int = self.__class__.id
        self.__class__.id += 1
    
    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours * 60)
    
    @staticmethod
    def get_next_id() -> int:
        return ExercisePlan.id
    
    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
    
