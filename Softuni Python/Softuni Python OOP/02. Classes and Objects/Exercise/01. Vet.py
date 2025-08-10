class Vet:
    animals: list[str] = []
    space: int = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    @classmethod
    def check_available(cls) -> int:
        return cls.space - len(cls.animals)
    
    @classmethod
    def cls_unregister_animal(cls, animal_name: str) -> bool:
        if animal_name in cls.animals:
            cls.animals.remove(animal_name)
            return True
        return False
    
    def register_animal(self, animal_name: str) -> str:
        if Vet.check_available() > 0:
            Vet.animals += [animal_name]
            self.animals += [animal_name]
            return f"{animal_name} registered in the clinic"
        return "Not enough space"
    
    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in Vet.animals and animal_name in self.animals:
            Vet.cls_unregister_animal(animal_name)
            self.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"
    
    def info(self) -> str:
        return f"{self.name} has {len(self.animals)} animals. {Vet.check_available()} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())     