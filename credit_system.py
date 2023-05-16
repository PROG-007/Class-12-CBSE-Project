class CreditCard:
    def __init__(self, card_number, credit_limit, balance=0):
        self.card_number = card_number
        self.credit_limit = credit_limit
        self.balance = balance

    def charge(self, amount):
        if amount > 0:
            if self.balance + amount <= self.credit_limit:
                self.balance += amount
                print(f"Charged {amount} to Credit Card {self.card_number}.")
                self.print_balance()
            else:
                print("Exceeded credit limit.")
        else:
            print("Invalid amount for charge.")

    def pay(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Paid {amount} for Credit Card {self.card_number}.")
                self.print_balance()
            else:
                print("Invalid payment amount.")
        else:
            print("Invalid amount for payment.")

    def print_balance(self):
        print(f"Credit Card {self.card_number} balance: {self.balance}")
