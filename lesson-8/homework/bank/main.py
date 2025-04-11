from bank import Bank

menu_text = """1. Create account
2. View Account
3. Deposit
4. Withdraw
5. Save
6. Exit
Enter menu choice: """

bank = Bank("accounts.txt")


def create_account():
    name = input("Enter name: ")
    initial_deposit = int(input("Enter initial deposit: "))
    account_number = bank.create_account(name, initial_deposit)
    print(f"Account created: {account_number}")
    print()


def view_account():
    account_number = int(input("Enter account number: "))
    account = bank.get_account(account_number)
    print()
    print(f"Account number: {account.account_number}")
    print(f"Account owner: {account.name}")
    print(f"Account balance: {account.balance}")
    print()


def deposit():
    account_number = int(input("Enter account number: "))
    amount = int(input("Enter deposit amount: "))
    bank.deposit(account_number, amount)
    print("Deposit successful")
    print()


def withdraw():
    account_number = int(input("Enter account number: "))
    amount = int(input("Enter withdrawal amount: "))
    bank.withdraw(account_number, amount)
    print("Withdraw successful")
    print()


def save():
    bank.save_to_file()
    print("Changes saved")
    print()


while True:
    option = int(input(menu_text))
    if option not in range(1, 7):
        print()
        print("Invalid menu choice")
        continue
    match option:
        case 1:
            create_account()
        case 2:
            view_account()
        case 3:
            deposit()
        case 4:
            withdraw()
        case 5:
            save()
        case 6:
            break
