class Person:
    def __init__(self, name: str, surname: str):
        self.name: str = name
        self.surname: str = surname
    
    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"
    
    def __add__(self, other):
        return Person(self.name, other.surname)

class Group:
    def __init__(self, name: str, people: list[Person]):
        self.name: str = name
        self.people: list[Person] = people
    
    def __add__(self, other):
        return self.__class__(f"{self.name} {other.name}", self.people + other.people)
    
    def __len__(self):
        return len(self.people)
    
    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]!r}"
    
    def __iter__(self):
        for index, person in enumerate(self.people):
            yield f"Person {index}: {person!r}"
    
    def __repr__(self):
        return f"Group {self.name} with members {', '.join(map(str, self.people))}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[2])

for person in third_group:
    print(person)