import random

import exceptions
from account import Account


class Bank:
    def __init__(self, file_name:str):
        self.__file_name = file_name
        self.__accounts = self.load_accounts()

    def create_account(self, name, initial_deposit):
        account_number = self.generate_account_number()
        new_account = Account(account_number, name, initial_deposit)
        self.__accounts.append(new_account)
        return account_number

    def get_account(self, account_number):
        for account in self.__accounts:
            if account.account_number == account_number:
                return account
        raise exceptions.AccountNotFoundException

    def deposit(self, account_number, deposit_amount:int):
        if deposit_amount <= 0:
            raise exceptions.InvalidDepositAmountException
        current_account = self.get_account(account_number)
        new_account = Account(account_number, current_account.name, current_account.balance + deposit_amount)
        self.__accounts.remove(current_account)
        self.__accounts.append(new_account)

    def withdraw(self, account_number, withdraw_amount:int):
        current_account = self.get_account(account_number)
        if current_account.balance < withdraw_amount:
            raise exceptions.InsufficientFundsException
        new_account = Account(account_number, current_account.name, current_account.balance - withdraw_amount)
        self.__accounts.remove(current_account)
        self.__accounts.append(new_account)

    def load_accounts(self):
        accounts = []
        try:
            with open(self.__file_name) as file:
                for row in file.readlines():
                    data = row.strip().split(",")
                    account_number = int(data[0])
                    name = data[1]
                    balance = int(data[2])
                    account = Account(account_number, name, balance)
                    accounts.append(account)
            return accounts
        except FileNotFoundError:
            with open(self.__file_name, "w"):
                pass
            return []

    def save_to_file(self):
        data = ""
        for account in self.__accounts:
            data += f"{account.account_number}, {account.name}, {account.balance}\n"
        data = data.strip()
        with open(self.__file_name, "w") as file:
            file.write(data)


    def generate_account_number(self):
        unavailable = [account.account_number for account in self.__accounts]
        new = random.randint(1000000, 9999999)
        while new in unavailable:
            new = random.randint(1000000, 9999999)
        return new
