from project.computer_types import Computer, DesktopComputer, Laptop

class ComputerStoreApp:
    VALID_TYPES = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop
    }
    def __init__(self):
        self.warehouse: list[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        computer: Computer = self.VALID_TYPES[type_computer](manufacturer, model)
        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return result
    
    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = next((comp for comp in self.warehouse if comp.price <= client_budget \
                        and comp.processor == wanted_processor and comp.ram >= wanted_ram), None)
        if not computer:
            raise Exception("Sorry, we don't have a computer for you.")
        
        self.profits += client_budget - computer.price

        self.warehouse.remove(computer)

        return f"{computer} sold for {client_budget}$."

