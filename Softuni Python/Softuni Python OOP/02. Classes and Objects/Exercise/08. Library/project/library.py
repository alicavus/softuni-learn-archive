from project.user import User

class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str, list[str]] = {}
        self.rented_books: dict[str, dict[str, int]] = {}
    
    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available and book_name in self.books_available[author]:
            user.books += [book_name]
            self.books_available[author].remove(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for renter_user in self.rented_books:
            if book_name in self.rented_books[renter_user]:
                return f"The book \"{book_name}\" is already rented and will be available in {self.rented_books[renter_user][book_name]} days!"
    
    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            if author not in self.books_available:
                self.books_available[author] = []
            self.books_available[author] += [book_name]
            self.rented_books[user.username].pop(book_name)
            user.books.remove(book_name)
            return
        return f"{user.username} doesn't have this book in his/her records!"
    

        


