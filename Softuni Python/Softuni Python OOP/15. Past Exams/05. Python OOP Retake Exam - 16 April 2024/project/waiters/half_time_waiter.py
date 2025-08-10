from project.waiters.base_waiter import BaseWaiter

class HalfTimeWaiter(BaseWaiter):
    @property
    def _data(selfself):
        return {
            "shift type": "half-time",
            "hourly wage": 12.0
        }
    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)
