import credit_system as c
import liability_system as l
import random

class User:
    def __init__(self, uid, email, password):
        self.uid = uid
        self.email = email
        self.password = password
        self.bank_account = l.BankAccount(f"{random.randint(10000000,99999999)}", uid, 100000)
        self.credit_card = c.CreditCard(f"{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}", uid, 10000)

    def login(self, email, password):
        if email == self.email and password == self.password:
            print("Login successful.")
            return True
        else:
            print("Invalid login credentials.")
            return False