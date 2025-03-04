# Rewrite the code to comply with SOLID principles

import logging
from abc import ABC, abstractmethod
from typing import List


# Login settings
logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler("program.log"),
        logging.StreamHandler()
    ]
)

class Logger:
    """Class for handling logging."""

    @staticmethod
    def log(message: str) -> None:
        logging.info(message)

class Book:
    """Class representing a book"""

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'


class LibraryInterface(ABC):
    """Interface for the library"""

    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    """Library book management class"""

    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        Logger.log(f"Book '{book.title}' added.")

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                Logger.log(f"Book '{title}' removed.")
                return
        Logger.log(f"Book '{title}' not found.")        


    def show_books(self) -> None:
        if not self.books:
            Logger.log(f"Library is empty.")
        else:
            for book in self.books:
                Logger.log(book.info())
 
class LibraryManager:
    """Class for managing the library via the command line interface"""

    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
         self.library.remove_book(title)  

    def show_books(self) -> None:
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                try:
                    year = int(input("Enter book year: ").strip())
                    manager.add_book(title, author, year)
                except ValueError:
                    Logger.log("Invalid year. Please enter a numeric value.")
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                Logger.log(f"Invalid command. Please try again.")

if __name__ == "__main__":
    main()