class Person:
    def __init__(self, name: str, age: int):
        self.__name: str = name
        self.__age: int = age
    
    def get_age(self) -> int:
        return self.__age
    
    def get_name(self) -> str:
        return self.__name


person = Person("George", 32)
print(person.get_name())
print(person.get_age())