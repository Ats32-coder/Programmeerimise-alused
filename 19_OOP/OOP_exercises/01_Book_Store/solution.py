"""Book store."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        :param name: book store name
        :param rating: store rating
        """
        self.name = name
        self.rating = rating
        self.books = []

    def can_add_book(self, book: Book) -> bool:
        """Check if book can be added."""
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                return False
        return book.rating >= self.rating

    def add_book(self, book: Book):
        """Add new book to book store if possible."""
        if self.can_add_book(book):
            self.books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """Check if book can be removed from store."""
        return book in self.books

    def remove_book(self, book: Book):
        """Remove book from store if possible."""
        if self.can_remove_book(book):
            self.books.remove(book)

    def get_all_books(self) -> list:
        """Return all books."""
        return self.books[::]

    def get_books_by_price(self) -> list:
        """Return books sorted by price (cheapest first)."""
        return sorted(self.books, key=lambda book: book.price)

    def get_most_popular_book(self) -> list:
        """Return book(s) with highest rating."""
        if not self.books:
            return []

        max_rating = max(book.rating for book in self.books)
        return [book for book in self.books if book.rating == max_rating]
