import credit_system as c
import liability_system as l
import random


class User:
    def __init__(self, email, password, uid=random.randint(1000000000, 9999999999)):
        self.uid = uid
        self.email = email
        self.password = password
        self.bank_account = l.BankAccount(
            f"{random.randint(10000000,99999999)}", self.uid, 100000, 10000)
        self.credit_card = c.CreditCard(
            f"{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}", self.uid, 2500000, 250000)
