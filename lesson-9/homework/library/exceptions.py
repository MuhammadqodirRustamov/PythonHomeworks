class LibraryException(Exception):
    def __init__(self, message):
        super().__init__(message)


class BookNotFoundException(LibraryException):
    def __init__(self):
        message = "Book not found"
        super().__init__(message)


class BookAlreadyBorrowedException(LibraryException):
    def __init__(self):
        message = "Book already borrowed"
        super().__init__(message)


class MemberLimitExceededException(LibraryException):
    def __init__(self):
        message = "Member limit exceeded"
        super().__init__(message)
