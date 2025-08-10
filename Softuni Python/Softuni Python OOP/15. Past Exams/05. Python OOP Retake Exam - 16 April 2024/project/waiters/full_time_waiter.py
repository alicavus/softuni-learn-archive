from project.waiters.base_waiter import BaseWaiter

class FullTimeWaiter(BaseWaiter):
    @property
    def _data(selfself):
        return {
            "shift type": "full-time",
            "hourly wage": 15.0
        }

    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)