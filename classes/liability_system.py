class BankAccount:
    def __init__(self, account_number, uid, withdraw_limit, balance=0):
        self.account_number = account_number
        self.uid = uid
        self.withdraw_limit = withdraw_limit
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount} to Account {self.account_number}."
        else:
            return "Invalid amount for deposit."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance <= amount:
                return "Insufficient funds."
            elif self.withdraw_limit < amount:
                return "Exceeded withdrawal limit."
            else:
                self.balance -= amount
                return f"Withdrew {amount} from Account {self.account_number}."
        else:
            return "Invalid amount for withdrawal."
