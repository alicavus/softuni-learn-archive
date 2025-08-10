class Band:
    def __init__(self, name: str):
        self.name: str = name
        self.members: list = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Band name should contain at least one character!")
        self._name: str = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."

    def get_musician_types(self):
        return set(member.__class__.__name__ for member in self.members)
