class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

def older_book(book1: Book, book2: Book):
    if book1.year < book2.year:
        print(f"The older book is '{book1.name}' by {book1.author}, published in {book1.year}.")
    elif book2.year < book1.year:
        print(f"The older book is '{book2.name}' by {book2.author}, published in {book2.year}.")
    else:
        print(f"Both books, '{book1.name}' by {book1.author} and '{book2.name}' by {book2.author}, were published in the same year ({book1.year}).")

# Example of the function in action
python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

older_book(python, everest)
older_book(python, norma)
