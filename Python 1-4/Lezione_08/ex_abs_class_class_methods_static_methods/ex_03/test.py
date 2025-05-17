from LibraryManager import *

book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia: Book = Book.from_string(book_str)
print(divina_commedia)

m1: Member = Member("Cristiano", 11122)
m1.borrow_book(divina_commedia)
print(f"\nChiedo in prestito un libro...\nLista libri in prestito da {m1.name}:\n", [b.title for b in m1.borrowed_books])
# m1.borrow_book(divina_commedia)
# m1.return_book(Book("Ciao", "c", 0))
m1.return_book(divina_commedia)
print(f"\nRitornando un libro...\nLista libri in prestito da {m1.name}:\n",[b.title for b in m1.borrowed_books])

print()
m2: Member = Member.from_string("Giacomo, 101")
print(m2)

book1 = Book("1984", "George Orwell", 123456789)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 987654321)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 112233445)
library1: Library = Library()


print("\n----------------------\nTrying to add a book\n---------------------")
library1.add_book(divina_commedia)
# library1.add_book(divina_commedia)
print(library1)

print("\n----------------------\nTrying to remove a book\n---------------------")
# library1.remove_book(book2)
library1.remove_book(divina_commedia)
print(library1)

library1.add_book(divina_commedia)
library1.add_book(book1)
library1.add_book(book2)

print("\n----------------------\nTrying to register a member\n---------------------")
library1.register_member(m1)
# library1.register_member(m1)
print(library1)

print()
library1.library_statistics()
# library1.lend_book(m2, book2)
# library1.lend_book(m1, book3)
library1.lend_book(m1, book2)
print(f"Lista libri in prestito da {m1.name}:\n", [bb.title for bb in m1.borrowed_books])
m1.return_book(book2)

# Two members borrow the same book
print()
m1.borrow_book(book1)
# m2.borrow_book(book1)
print(f"Lista libri in prestito da {m1.name}:\n", [bb.title for bb in m1.borrowed_books])
print(f"Lista libri in prestito da {m2.name}:\n", [bb.title for bb in m2.borrowed_books])

print()
m1.return_book(book1)
m2.borrow_book(book1)
print(f"Lista libri in prestito da {m1.name}:\n", [bb.title for bb in m1.borrowed_books])
print(f"Lista libri in prestito da {m2.name}:\n", [bb.title for bb in m2.borrowed_books])
