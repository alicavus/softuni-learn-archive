from project.loans.base_loan import BaseLoan

class MortgageLoan(BaseLoan):
    @property
    def _data(self) -> dict:
        return {
            "interest rate": 3.5,
            "amount": 50_000.0,
            "increase interest": 0.5
        }
    def __init__(self):
        super().__init__(self._data.get("interest rate", 0), self._data.get("amount", 0))