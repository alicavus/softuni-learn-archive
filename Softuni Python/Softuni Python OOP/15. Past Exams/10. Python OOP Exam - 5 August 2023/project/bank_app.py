from os import remove

from project.clients.base_client import BaseClient
from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan

class BankApp:
    CLIENT_TYPES = {
        "Adult": Adult,
        "Student": Student
    }
    LOAN_TYPES = {
        "MortgageLoan": MortgageLoan,
        "StudentLoan": StudentLoan
    }
    LOAN_TYPES_FOR_CLIENT_TYPES = {
        Adult: MortgageLoan,
        Student: StudentLoan
    }
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.clients: list[BaseClient] = []
        self.loans: list[BaseLoan] = []

    def add_loan(self, loan_type: str):
        cls = self.LOAN_TYPES.get(loan_type, None)
        if cls is None:
            raise Exception("Invalid loan type!")
        self.loans.append(cls())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        cls = self.CLIENT_TYPES.get(client_type, None)
        client: BaseClient = self.get_item(self.clients, "client_id", client_id)

        if cls is None:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        self.clients.append(cls(client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client: BaseClient = self.get_item(self.clients, "client_id", client_id)
        loan: BaseLoan = self.get_item(self.loans, "__class__", self.LOAN_TYPES.get(loan_type, None))

        if client is None or loan is None:
            return

        if self.LOAN_TYPES_FOR_CLIENT_TYPES.get(client.__class__, None) != loan.__class__:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client: BaseClient = self.get_item(self.clients, "client_id", client_id)

        if client is None:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        count = 0
        loans = self.get_items(self.loans, "__class__", self.LOAN_TYPES.get(loan_type, None))
        for loan in loans:
            loan.increase_interest_rate()
            count += 1
        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate: float):
        count = 0
        for client in self.get_items(self.clients):
            if client.interest < min_rate:
                client.increase_clients_interest()
                count += 1
        return f"Number of clients affected: {count}."

    def get_statistics(self):
        total_clients_count = 0
        total_clients_income = 0
        loans_count_granted_to_clients = 0
        granted_sum = 0
        loans_count_not_granted = 0
        not_granted_sum = 0
        avg_client_interest_rate = 0
        for client in self.get_items(self.clients):
            total_clients_count += 1
            total_clients_income += client.income
            avg_client_interest_rate += client.interest
            for loan in self.get_items(client.loans):
                loans_count_granted_to_clients += 1
                granted_sum += loan.amount
        avg_client_interest_rate /= 1 if total_clients_count == 0 else total_clients_count
        for loan in self.get_items(self.loans):
            loans_count_not_granted += 1
            not_granted_sum += loan.amount
        return f"""Active Clients: {total_clients_count}
Total Income: {total_clients_income:.2f}
Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}
Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}
Average Client Interest Rate: {avg_client_interest_rate:.2f}"""






    @staticmethod
    def get_item(collection, attribute_name = None, attribute_value = None):
        if attribute_name is None:
            return next((item for item in collection), None)
        return next((item for item in collection if getattr(item, attribute_name, None) == attribute_value), None)

    @staticmethod
    def get_items(collection, attribute_name = None, attribute_value = None):
        if attribute_name is None:
            return (item for item in collection)
        return (item for item in collection if getattr(item, attribute_name, None) == attribute_value)
