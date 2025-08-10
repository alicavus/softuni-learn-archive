from project.loans.base_loan import BaseLoan

class StudentLoan(BaseLoan):
    @property
    def _data(self) -> dict:
        return {
            "interest rate": 1.5,
            "amount": 2_000.0,
            "increase interest": 0.2
        }
    def __init__(self):
        super().__init__(self._data.get("interest rate", 0), self._data.get("amount", 0))