class Worker:
    '''Base class for Zoo personel'''
    def __init__(self, name: str, age: int, salary: int):
        self.name: str = name
        self.age: int = age
        self.salary: int = salary

    def __repr__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
    
    