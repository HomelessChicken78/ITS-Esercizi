class Book:
    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

    def __str__(self) -> str:
        return f"\"{self.title}\" by {self.author} | {self.isbn}"
    
    @classmethod
    def from_string(cls, string: str):
        l: list[str, str, int] = string.split(", ")
        l[2] = int(l[2])
        return cls(l[0], l[1], l[2])

class Member:
    def __init__(self, name: str, member_id: int):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book: Book) -> None:
        '''Add a book to the borrowed_books list.'''
        if not isinstance(book, Book):
            raise ValueError(f"{book} is not an instance of the class \"Book\"")
        if book in self.borrowed_books:
            raise ValueError(f"The book \"{book.title}\" ({book.isbn}) is already present in the borrowed book list of {self.name}.")
        if book.borrowed:
            raise ValueError(f"The book \"{book.title}\" ({book.isbn}) has already been lent")
        self.borrowed_books.append(book)
        book.borrowed = True
    
    def return_book(self, book: Book) -> None:
        '''Remove a book from the borrowed_books list.'''
        if not isinstance(book, Book):
            raise ValueError(f"{book} is not an instance of the class \"Book\"")
        if book not in self.borrowed_books:
            raise ValueError(f"The book \"{book.title}\" ({book.isbn}) has never been borrowed by {self.name}.")
        self.borrowed_books.remove(book)
        book.borrowed = False
    
    def __str__(self) -> str:
        return f"{self.name} ({self.member_id})"
    
    @classmethod
    def from_string(cls, string: str):
        l: list[str, int] = string.split(", ")
        l[1] = int(l[1])
        return cls(l[0], l[1])
    
class Library:
    total_books = 0

    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book: Book):
        '''Add a book to the library.'''
        if not isinstance(book, Book):
            raise ValueError(f"{book} is not an instance of the class \"Book\"")
        if book in self.books:
            raise ValueError(f"The book \"{book.title}\" ({book.isbn}) is already present in the library.")
        self.books.append(book)
        Library.total_books += 1

    def remove_book(self, book: Book):
        '''Remove a book from the library.'''
        if not isinstance(book, Book):
            raise ValueError(f"{book} is not an instance of the class \"Book\"")
        if book not in self.books:
            raise ValueError(f"The book \"{book.title}\" ({book.isbn}) isn't present in the library.")
        self.books.remove(book)
        Library.total_books -= 1

    def register_member(self, member: Member):
        '''Add a member to the library.'''
        if not isinstance(member, Member):
            raise ValueError(f"{member} is not an instance of the class \"Member\"")
        if member in self.members:
            raise ValueError(f"The member \"{member.name}\" ({member.member_id}) is already registered to the library.")
        self.members.append(member)

    def lend_book(self, member: Member, book: Book):
        '''Lend a book to a member. Check if the book is available and if the member is registered.'''
        if not isinstance(member, Member):
            raise ValueError(f"{member} is not an instance of the class \"Member\"")
        if not isinstance(book, Book):
            raise ValueError(f"{book} is not an instance of the class \"Book\"")
        
        if book not in self.books:
            raise ValueError(f"The book \"{book.title}\" ({book.isbn}) isn't present in the library.")
        if member not in self.members:
            raise ValueError(f"The member \"{member.name}\" ({member.member_id}) isn't registered to the library.")
        
        member.borrow_book(book)

    def __str__(self) -> str:
        return f"Books:\n{[b.title for b in self.books]}\n\nMembers:\n{[m.name for m in self.members]}"

    @classmethod
    def library_statistics(cls):
        '''Print the total number of books.'''
        print(cls.total_books)