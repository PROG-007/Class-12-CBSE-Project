class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to Account {self.account_number}.")
            self.print_balance()
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} from Account {self.account_number}.")
                self.print_balance()
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount for withdrawal.")

    def print_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")
