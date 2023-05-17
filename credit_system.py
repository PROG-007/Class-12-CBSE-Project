class CreditCard:
    def __init__(self, card_number, uid, credit_limit, spend_limit, balance=0):
        self.card_number = card_number
        self.uid = uid
        self.credit_limit = credit_limit
        self.spend_limit = spend_limit
        self.balance = balance

    def charge(self, amount):
        if amount > 0:
            if self.balance + amount <= self.credit_limit:
                print("Exceeded credit limit.")
            elif amount <= self.spend_limit:
                print("Exceeded spend limit.")
            else:
                self.balance += amount
                print(f"Charged {amount} to Credit Card {self.card_number}.")
                self.print_balance()
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
        print(
            f"Credit Card no. {self.card_number} => Current Bill : {self.balance}")
