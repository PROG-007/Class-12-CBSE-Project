import credit_system as c
import liability_system as l
import random

class User:
    def __init__(self, email, password):
        self.uid = random.randint(1000000000,9999999999)
        self.email = email
        self.password = password
        self.bank_account = l.BankAccount(f"{random.randint(10000000,99999999)}", self.uid, 100000)
        self.credit_card = c.CreditCard(f"{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}", self.uid, 10000)

    def login(self, email, password):
        if email == self.email and password == self.password:
            print(f"Login successful. {self.uid}")
            return True
        else:
            print("Invalid login credentials.")
            return False