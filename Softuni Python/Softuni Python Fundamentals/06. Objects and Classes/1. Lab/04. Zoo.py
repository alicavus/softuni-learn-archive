class Zoo:
    __animals = 0 #Private attribute

    def __init__(self, name: str):
        self.name = name
        self.mammals, self.fishes, self.birds = [[]] * 3
    
    def add_animal(self, species: str, name: str):
        attr = species 
        attr += 's' if species != "fish" else 'es'
        setattr(self, attr, getattr(self, attr) + [name])
        self.__animals += 1
    
    def get_info(self, specy):
        attr = specy
        attr += 's' if specy != "fish" else 'es'
        return f"""{attr.capitalize()} in {self.name}: {", ".join(getattr(self, attr))}
Total animals: {len([x for x in self.mammals + self.fishes + self.birds])}"""

zoo = Zoo(input())
animal_count = int(input())

for _ in range(animal_count):
    animal_species, animal_name = input().split()
    zoo.add_animal(species=animal_species, name=animal_name)

print(zoo.get_info(input()))
