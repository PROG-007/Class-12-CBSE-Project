from classes.credit_system import CreditCard
from classes.liability_system import BankAccount
import random


class User:
    def __init__(self, email, password, uid=random.randint(1000000000, 9999999999)):
        self.uid = uid
        self.email = email
        self.password = password
        self.bank_account = BankAccount(
            f"{random.randint(10000000,99999999)}", self.uid, 100000, 10000)
        self.credit_card = CreditCard(
            f"{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}", self.uid, 2500000, 250000)
        
        
    def refresh_data(self, database):
        account_data = database.get_account(self.uid)
        if account_data:
            account_number, withdraw_limit, balance = account_data
            self.bank_account = BankAccount(account_number, withdraw_limit, balance)

        credit_card_data = database.get_credit_card(self.uid)
        if credit_card_data:
            card_number, credit_limit, spend_limit, due = credit_card_data
            self.credit_card = CreditCard(card_number, credit_limit, spend_limit, due)
