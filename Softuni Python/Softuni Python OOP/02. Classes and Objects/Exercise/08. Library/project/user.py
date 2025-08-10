class User:
    def __init__(self, user_id: int, username: str):
        self.user_id: int = user_id
        self.username: str = username
        self.books: list[str] = []
    
    def __str__(self) -> str:
        return f"{self.user_id}, {self.username}, {self.books}"
    
    def info(self) -> str:
        return ", ".join(sorted(self.books))