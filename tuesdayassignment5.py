class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

# Example of creating an instance of the Book class
my_book = Book(name="To Kill a Mockingbird", author="Harper Lee", genre="Fiction", year=1960)

print(f"Book: {my_book.name}, Author: {my_book.author}, Genre: {my_book.genre}, Year: {my_book.year}")
