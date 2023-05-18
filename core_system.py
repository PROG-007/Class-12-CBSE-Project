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
        return uid
    else:
        print("Invalid login credentials.")
        return None


def handle_signup(database):
    cls()
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")

    uid = database.insert_user(email_input, password_input)
    if uid is not None:
        print("Account created successfully.")
        print("###Account SETUP###")
        withdraw_limit = float(input("Enter the withdraw limit: "))
        balance = float(input("Enter the initial balance: "))
        database.insert_account(uid, withdraw_limit, balance)
        print("###Credit Card SETUP###")
        credit_limit = float(input("Enter the credit limit: "))
        spend_limit = float(input("Enter the spend limit: "))
        database.insert_credit_card(
            uid , credit_limit, spend_limit, 0)

        return uid
    else:
        print("Failed to create an account.")
        return None


def print_main_menu():
    print("\nMain Menu:")
    print("1. Manage Bank Account")
    print("2. Manage Credit Card")
    print("3. Logout")


def handle_main_menu(database, uid):
    bank_account = None
    credit_card = None

    # Retrieve account details from the database
    account_details = database.get_account(uid)
    if account_details is not None:
        account_number, withdraw_limit, balance = account_details
        bank_account = BankAccount(
            account_number, uid, withdraw_limit, balance)

    # Create a temporary CreditCard object (does not retrieve from database)
    credit_card = CreditCard("", uid, 2500000, 250000)

    user = User("", "", uid)
    user.bank_account = bank_account
    user.credit_card = credit_card

    while True:
        cls()
        print_main_menu()
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
    print("3. Check Balance")
    print("4. Print Account Details")
    print("5. Back")


def handle_bank_account_menu(user, database):
    while True:
        cls()
        print_bank_account_menu()
        bank_choice = int(input("Enter your choice: "))
        if bank_choice == 1:
            amount = float(input("Enter the amount to withdraw: "))
            user.bank_account.withdraw(amount)
            database.update_account_balance(
                user.uid, user.bank_account.balance)
        elif bank_choice == 2:
            amount = float(input("Enter the amount to deposit: "))
            user.bank_account.deposit(amount)
            database.update_account_balance(
                user.uid, user.bank_account.balance)
        elif bank_choice == 3:
            account_number, withdraw_limit, balance = database.get_account(
                user.uid)
            print("Account Number:", account_number)
            print("Withdraw Limit:", withdraw_limit)
            print("Current Balance:", balance)
        elif bank_choice == 4:
            print("Account Number:", user.bank_account.account_number)
            user.bank_account.print_balance()
        elif bank_choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")
        next()


def print_credit_card_menu():
    print("\nCredit Card Menu:")
    print("1. Pay Bill")
    print("2. Charge")
    print("3. Check Total Due Bill")
    print("4. Back")


def handle_credit_card_menu(user, database):
    while True:
        cls()
        print_credit_card_menu()
        credit_choice = int(input("Enter your choice: "))
        if credit_choice == 1:
            amount = float(input("Enter the amount to pay: "))
            user.credit_card.pay(amount)
            user.credit_card.print_balance()
        elif credit_choice == 2:
            amount = float(input("Enter the amount to charge: "))
            user.credit_card.charge(amount)
            user.credit_card.print_balance()
        elif credit_choice == 3:
            credit_card_info = database.get_credit_card(user.uid)
            if credit_card_info is not None:
                card_number, credit_limit, due = credit_card_info
                print("Card Number:", card_number)
                print("Credit Limit:", credit_limit)
                print("Current Due:", due)
            else:
                print("No credit card information found.")
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
        uid = handle_login(database)
        if uid is not None:
            handle_main_menu(database, uid)

    elif choice == 2:
        uid = handle_signup(database)
        if uid is not None:
            handle_main_menu(database, uid)

    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")

database.close()