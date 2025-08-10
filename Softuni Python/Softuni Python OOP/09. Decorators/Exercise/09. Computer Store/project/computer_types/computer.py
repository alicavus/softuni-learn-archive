from abc import ABC, abstractmethod

class Computer(ABC):
    @property
    @abstractmethod
    def CPU(self):
        pass

    @property
    @abstractmethod
    def MAX_RAM(self):
        pass

    @property
    def VALID_RAMSIZE(self):
        power = 1
        result = 2
        res = {}
        while result <= self.MAX_RAM:
            res[result] = power * 100
            result *= 2
            power += 1
        return res
    
    @property
    @abstractmethod
    def computer_type(self):
        pass

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str = None
        self.ram: int = None
        self.price: int = 0
    
    @property
    def manufacturer(self) -> str:
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value or value.isspace():
            raise ValueError("Manufacturer name cannot be empty.")
        self._manufacturer = value
    
    @property
    def model(self) -> str:
        return self._model
    
    @model.setter
    def model(self, value):
        if not value or value.isspace():
            raise ValueError("Model name cannot be empty.")
        self._model = value
    
    def configure_computer(self, processor: str, ram: int):
        if processor not in self.CPU:
            raise ValueError(f"{processor} is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")
        
        if ram not in self.VALID_RAMSIZE:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")
        
        self.processor = processor
        self.ram = ram

        self.price += self.CPU[processor] + self.VALID_RAMSIZE[ram]

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."


    def __repr__(self) -> str:
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"


