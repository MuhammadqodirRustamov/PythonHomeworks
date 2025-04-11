class BankingException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InsufficientFundsException(BankingException):
    message = "No enough funds in the account"

    def __init__(self):
        super().__init__(self.message)


class AccountNotFoundException(BankingException):
    message = "Account not found"

    def __init__(self):
        super().__init__(self.message)


class InvalidDepositAmountException(BankingException):
    message = "Invalid deposit amount"

    def __init__(self):
        super().__init__(self.message)
