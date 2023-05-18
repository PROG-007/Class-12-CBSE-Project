class BankAccount:
    def __init__(self, account_number, uid, withdraw_limit, balance=0):
        self.account_number = account_number
        self.uid = uid
        self.withdraw_limit = withdraw_limit
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
            if self.balance <= amount:
                print("Insufficient funds.")
            elif self.withdraw < amount:
                print("Exceeded withdrawal limit.")
            else:
                self.balance -= amount
                print(f"Withdrew {amount} from Account {self.account_number}.")
                self.print_balance()
        else:
            print("Invalid amount for withdrawal.")

    def print_balance(self):
        print(f"Current Balance : {self.balance}")

