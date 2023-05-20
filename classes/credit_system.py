class CreditCard:
    def __init__(self, card_number, uid, credit_limit, spend_limit, due=0):
        self.card_number = card_number
        self.uid = uid
        self.credit_limit = credit_limit
        self.spend_limit = spend_limit
        self.due = due

    def charge(self, amount):
        if amount > 0:
            if self.due + amount > self.credit_limit:
                print("Exceeded credit limit.")
            elif amount > self.spend_limit:
                print("Exceeded spend limit.")
            else:
                self.due += amount
                print(f"Charged {amount} to Credit Card {self.card_number}.")
        else:
            print("Invalid amount for charge.")

    def pay(self, amount):
        if amount > 0:
            if self.due >= amount:
                self.due -= amount
                print(f"Paid {amount} for due of Credit Card {self.card_number}.")
            else:
                print("Invalid payment amount.")
        else:
            print("Invalid amount for payment.")
