# Aggregation ist eine Beziehung von Objekten zueinander, bei der die Teile ohne das Ganze existieren können. ('has a' Relationship, also "kann")
# Ein Objekt dient als Container(das Ganze) für die anderen Objekte (Teile). Dabei kann das Ganze auch ohne die Teile
# existieren und umgekehrt. 


class Library:                            # die Bibliothek kann ohne die Bücher existieren
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}"for book in self.books]


class Book:                               # die Bücher können ohne die Bibliothek auch existieren
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = Library("New York Public Library")

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit","J.R.R. Tolkin")
book3 = Book("The Colour of Magic","Terry Pratchett")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)

# print(library.list_books())

for book in library.list_books():
    print(book)
    

# Hier der Unterschied zu der Komposition. Wenn man das library Objekt zerstören würde, dann würden die book Objekte immer noch existieren.