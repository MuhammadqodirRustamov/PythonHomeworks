class Account:
    def __init__(self, account_number, name, initial_deposit):
        self.account_number:int = account_number
        self.name:str = name
        self.balance:int = initial_deposit
