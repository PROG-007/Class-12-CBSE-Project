import os
import db_mnger_cls
import liability_system
import credit_system
import user_system

Database = db_mnger_cls.Database
BankAccount = liability_system.BankAccount
CreditCard = credit_system.CreditCard
User = user_system.User


def print_auth_menu():
    print("1. Login")
    print("2. Create New Account")
    print("3. Exit")


def handle_login(database):
    cls()
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")

    uid = database.get_user(email_input, password_input)
    if uid is not None:
        print("Login successful.")
        return uid, email_input, password_input
    else:
        print(f"Incorrect credentials.")
        return None, email_input, password_input


def handle_signup(database):
    cls()
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")

    uid = database.insert_user(email_input, password_input)
    if uid is not None:
        print("Account created successfully.")
        print("\n### Account SETUP ###")
        withdraw_limit = float(input("Enter the withdraw limit: "))
        balance = float(input("Initial Deposit: "))
        database.insert_account(uid, withdraw_limit, balance)
        print("\n### Credit Card SETUP ###")
        credit_limit = 10000
        print(f"Credit Limit is {credit_limit} in a new account")
        spend_limit = float(input("Enter the spend limit: "))
        database.insert_credit_card(
            uid , credit_limit, spend_limit)

        return uid, email_input, password_input
    else:
        print(f"Failed to create an account")
        return None, email_input, password_input


def print_main_menu(uid):
    print(f"Logged in as User {uid}")
    print("\nMain Menu:")
    print("1. Manage Bank Account")
    print("2. Manage Credit Card")
    print("3. Logout")


def handle_main_menu(database, uid, email_input, password_input):
    bank_account = None
    credit_card = None

    # Retrieve account details from the database
    account_details = database.get_account(uid)
    if account_details is not None:
        account_number, withdraw_limit, balance = account_details
        bank_account = BankAccount(
            account_number, uid, withdraw_limit, balance)

    # Retrieve credit card details from the database
    credit_card = database.get_credit_card(uid)
    if credit_card is not None:
        card_number, credit_limit, spend_limit, due = credit_card
        credit_card = CreditCard(
            card_number, uid, credit_limit, spend_limit, due)

    user = User(email_input, password_input, uid)
    user.bank_account = bank_account
    user.credit_card = credit_card

    while True:
        cls()
        print_main_menu(uid)
        account_choice = int(input("Enter your choice: "))
        if account_choice == 1:
            handle_bank_account_menu(user, database)
        elif account_choice == 2:
            handle_credit_card_menu(user, database)
        elif account_choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")
        next()


def print_bank_account_menu():
    print("\nBank Account Menu:")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Print Account Details")
    print("4. Back")


def handle_bank_account_menu(user, database):
    while True:
        cls()
        print_bank_account_menu()
        bank_choice = int(input("Enter your choice: "))
        if bank_choice == 1:
            amount=0
            temp1 = float(input("Enter the amount to withdraw: "))
            temp2 = float(input("Re-Confirm the withdrawal amount: "))
            if temp1!=temp2:
                print("Amount entered does not match.")
            else:
                amount=temp1
                user.bank_account.withdraw(amount)
                database.update_account_balance(
                    user.uid, user.bank_account.balance)
        elif bank_choice == 2:
            amount = float(input("Enter the amount to deposit: "))
            user.bank_account.deposit(amount)
            database.update_account_balance(
                user.uid, user.bank_account.balance)
        elif bank_choice == 3:
            print("Account Number:", user.bank_account.account_number)
            print("Withdraw Limit:", user.bank_account.withdraw_limit)
            print("Current Balance:", user.bank_account.balance)
        elif bank_choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
        next()


def print_credit_card_menu():
    print("\nCredit Card Menu:")
    print("1. Pay Bill")
    print("2. Charge")
    print("3. Check Card Details")
    print("4. Back")


def handle_credit_card_menu(user, database):
    while True:
        cls()
        print_credit_card_menu()
        credit_choice = int(input("Enter your choice: "))
        if credit_choice == 1:
            amount = float(input("Enter the amount to pay: "))
            user.credit_card.pay(amount)
            database.update_credit_card_due(
                user.uid, user.credit_card.due)
        elif credit_choice == 2:
            amount = float(input("Enter the amount to charge: "))
            user.credit_card.charge(amount)
            database.update_credit_card_due(
                user.uid, user.credit_card.due)
        elif credit_choice == 3:
            print("Card Number:", user.credit_card.card_number)
            print("Credit Limit:", user.credit_card.credit_limit)
            print("Spend Limit:", user.credit_card.spend_limit)
            print("Current Due:", user.credit_card.due)
        elif credit_choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
        next()


database = Database()


def next():
    os.system('PAUSE')
    os.system('cls')


def cls():
    os.system('cls')

while True:
    cls()
    print_auth_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        uid, email_input, password_input = handle_login(database)
        if uid is not None:
            handle_main_menu(database, uid, email_input, password_input)

    elif choice == 2:
        uid, email_input, password_input = handle_signup(database)
        if uid is not None:
            handle_main_menu(database, uid, email_input, password_input)

    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")
    next()

database.close()