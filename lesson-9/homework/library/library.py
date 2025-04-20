from exceptions import BookAlreadyBorrowedException
from exceptions import BookNotFoundException
from exceptions import MemberLimitExceededException


class Library:
    def __init__(self):
        self.__books = []
        self.__members = []

    def add_book(self, book):
        self.__books.append(book)

    def add_member(self, member):
        self.__members.append(member)

    def borrow_check(self, member_id, book_id):
        for member in self.__members:
            if member.member_id == member_id:
                if len(member.borrowed_books) > 2:
                    raise MemberLimitExceededException
        for book in self.__books:
            if book.book_id == book_id:
                if book.is_borrowed:
                    raise BookAlreadyBorrowedException
                else:
                    return
        raise BookNotFoundException

    def borrow(self, member_id, book_id):
        self.borrow_check(member_id, book_id)
        for member in self.__members:
            if member.member_id == member_id:
                member.borrowed_books.append(book_id)
                break
        for book in self.__books:
            if book.book_id == book_id:
                book.is_borrowed = True
                break
        print(f"Member with id {member_id} borrowed book with id {book_id}")

    def return_book(self, member_id, book_id):
        for book in self.__books:
            if book.book_id == book_id:
                book.is_borrowed = False
                break
        for member in self.__members:
            if member.member_id == member_id:
                member.borrowed_books.remove(book_id)
                break
        print(f"Member with id {member_id} returned book with id {book_id}")

