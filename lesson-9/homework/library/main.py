from library import Library
from book import Book
from member import Member

library = Library()

book1 = Book(1, "Book 1", "Author 1", False)
book2 = Book(2, "Book 2", "Author 2", False)
book3 = Book(3, "Book 3", "Author 3", False)
book4 = Book(4, "Book 4", "Author 4", False)
book5 = Book(5, "Book 5", "Author 5", False)

member1 = Member(1, "Member 1")
member2 = Member(2, "Member 2")
member3 = Member(3, "Member 3")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

library.add_member(member1)
library.add_member(member2)
library.add_member(member3)

library.borrow(1, 1)
library.borrow(1, 2)
library.borrow(1, 3)
library.return_book(1, 1)
library.borrow(1, 4)
