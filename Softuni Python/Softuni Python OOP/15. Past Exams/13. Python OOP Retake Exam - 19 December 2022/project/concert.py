class Concert:
    ALLOWED_GENRES = "Metal", "Rock", "Jazz"
    AUDIENCE_MIN_ATTENDENTS = 1
    TICKET_PRICE_MIN_VALUE = 1.0
    PLACE_MIN_CHARS = 2

    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre: str = genre
        self.audience: int = audience
        self.ticket_price: float = ticket_price
        self.expenses: float = expenses
        self.place: str = place

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    def genre(self, value: str):
        if value not in self.ALLOWED_GENRES:
            raise ValueError(f"Our group doesn't play {value}!")
        self._genre: str = value

    @property
    def audience(self) -> int:
        return self._audience

    @audience.setter
    def audience(self, value: int):
        if value < self.AUDIENCE_MIN_ATTENDENTS:
            raise ValueError("At least one person should attend the concert!")
        self._audience: int = value

    @property
    def ticket_price(self) -> float:
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, value: float):
        if value < self.TICKET_PRICE_MIN_VALUE:
            raise ValueError(f"Ticket price must be at least {self.TICKET_PRICE_MIN_VALUE:.2f}$!")
        self._ticket_price: float = value

    @property
    def expenses(self) -> float:
        return self._expenses

    @expenses.setter
    def expenses(self, value: float):
        if value < 0.0:
            raise ValueError("Expenses cannot be a negative number!")
        self._expenses: float = value

    @property
    def place(self) -> str:
        return self._place

    @place.setter
    def place(self, value: str):
        if not value.strip() or len(value) < self.PLACE_MIN_CHARS:
            raise ValueError(f"Place must contain at least {self.PLACE_MIN_CHARS} chars. It cannot be empty!")
        self._place: str = value

    def calculate_profit(self):
        return self.audience * self.ticket_price - self.expenses

    def __str__(self) -> str:
        return f"{self.genre} concert at {self.place}."