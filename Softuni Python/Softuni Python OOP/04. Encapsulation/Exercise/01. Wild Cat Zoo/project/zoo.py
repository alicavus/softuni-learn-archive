from project.animal import Animal
from project.worker import Worker

class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name: str = name
        self.__budget: int = budget
        self.__animal_capacity: int = animal_capacity
        self.__workers_capacity: int = workers_capacity

        self.animals: list[Animal] = []
        self.workers: list[Worker] = []
    
    @property
    def get_animal_capacity(self) -> int:
        return self.__animal_capacity - len(self.animals)
    
    @property
    def get_worker_capacity(self) -> int:
        return self.__workers_capacity - len(self.workers)
    
    @property
    def get_total_salary(self) -> int:
        return sum(worker.salary for worker in self.workers) if self.workers else 0
    
    @property
    def get_animal_cost(self) -> int:
        return sum(animal.money_for_care for animal in self.animals) if self.animals else 0
    
    def add_animal(self, animal: Animal, price: int) -> str:
        if self.get_animal_capacity > 0:
            if self.__budget >= price:
                self.__budget -= price
                self.animals += [animal]
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"
    
    def hire_worker(self, worker: Worker) -> str:
        if self.get_worker_capacity > 0:
            self.workers += [worker]
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"
    
    def fire_worker(self, worker_name: str) -> str:
        for worker_idx, worker in enumerate(self.workers):
            if worker.name == worker_name:
                self.workers.pop(worker_idx)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"
    
    def pay_workers(self) -> str:
        if self.get_total_salary <= self.__budget:
            self.__budget -= self.get_total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"
    
    def tend_animals(self) -> str:
        if self.get_animal_cost <= self.__budget:
            self.__budget -= self.get_animal_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."
    
    def profit(self, amount: int):
        self.__budget += amount
    
    def animals_status(self) -> str:
        lions: list[str] = []
        tigers: list[str] = []
        cheetahs: list[str] = []
        for animal in self.animals:
            match animal.__class__.__name__:
                case "Lion":
                    lions += [animal.__repr__()]
                case "Tiger":
                    tigers += [animal.__repr__()]
                case "Cheetah":
                    cheetahs += [animal.__repr__()]
        res = [f"You have {len(self.animals)} animals"]
        for col in [lions, tigers, cheetahs]:
            res += [f'----- {len(col)} {"Lions" if col == lions else "Tigers" if col == tigers else "Cheetahs"}:']
            res.extend(col)
        
        return "\n".join(res)
    
    def workers_status(self) -> str:
        keepers: list[str] = []
        caretakers: list[str] = []
        vets: list[str] = []
        
        for worker in self.workers:
            match worker.__class__.__name__:
                case "Keeper":
                    keepers += [worker.__repr__()]
                case "Caretaker":
                    caretakers += [worker.__repr__()]
                case "Vet":
                    vets += [worker.__repr__()]
            res = [f"You have {len(self.workers)} workers"]

            for col in [keepers, caretakers, vets]:
                res += [f'----- {len(col)} {"Keepers" if col == keepers else "Caretakers" if col == caretakers else "Vets"}:']
                res.extend(col)
        
        return "\n".join(res)