"""
composition
"""
from book import Book


class Author:
    """Author class"""
    def __init__(self, name, books, title, author, pub_year):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.my_author = Book(name, books)
