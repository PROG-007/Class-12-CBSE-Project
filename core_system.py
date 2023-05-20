import os
from classes.db_mnger_cls import Database
from classes.user_system import User


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

    user = User(email_input, password_input, uid)

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
    print("3. Transfer Money Using UID")
    print("4. Print Account Details")
    print("5. Back")


def handle_bank_account_menu(user, database):
    while True:
        cls()
        print_bank_account_menu()
        bank_choice = int(input("Enter your choice: "))

        if bank_choice == 1:
            amount = 0
            temp1 = float(input("Enter the amount to withdraw: "))
            temp2 = float(input("Re-Confirm the withdrawal amount: "))
            if temp1 != temp2:
                print("Amount entered does not match.")
            else:
                amount = temp1
                user_balance = database.get_account(user.uid)
                if user_balance is None:
                    print("Error: Unable to fetch account balance.")
                elif amount > user_balance:
                    print("Insufficient balance.")
                elif amount > user.withdraw_limit:
                    print("Exceeded withdrawal limit.")
                else:
                    success = database.update_account_balance(user.uid, user_balance - amount)
                    if success:
                        print("Withdrawal successful.")
                    else:
                        print("Error: Failed to update account balance.")

        elif bank_choice == 2:
            amount = float(input("Enter the amount to deposit: "))
            user_balance = database.get_account(user.uid)
            if user_balance is None:
                print("Error: Unable to fetch account balance.")
            else:
                success = database.update_account_balance(user.uid, user_balance + amount)
                if success:
                    print("Deposit successful.")
                else:
                    print("Error: Failed to update account balance.")

        elif bank_choice == 3:
            recipient_uid = input("Enter the recipient's UID: ")
            amount = 0
            temp1 = float(input("Enter the amount to transfer: "))
            temp2 = float(input("Re-Confirm the transfer amount: "))
            if temp1 != temp2:
                print("Amount entered does not match.")
            else:
                amount = temp1
                transfer_result = database.transfer_money(user.uid, recipient_uid, amount)
                if transfer_result is True:
                    print(f"Transfer of {amount} to {recipient_uid} was successful.")
                else:
                    print(f"Transfer to {recipient_uid} NOT SUCCESSFUL - {transfer_result}")

        elif bank_choice == 4:
            account_number, withdraw_limit, balance = database.get_account(user.uid)
            if account_number:
                print("Account Number:", account_number)
                print("Withdraw Limit:", withdraw_limit)
                print("Balance:", balance)
            else:
                print("Bank Account details not found for the user.")

        elif bank_choice == 5:
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
        user.refresh_data(database)
        cls()
        print_credit_card_menu()
        credit_choice = int(input("Enter your choice: "))

        if credit_choice == 1:
            amount = float(input("Enter the amount to pay: "))
            if amount > 0:
                if user.credit_due >= amount:
                    user.credit_due -= amount
                    database.update_credit_card_due(user.uid, user.credit_due)
                    print(f"Paid {amount} for due of Credit Card {user.credit_card_number}.")
                else:
                    print("Invalid payment amount.")
            else:
                print("Invalid amount for payment.")

        elif credit_choice == 2:
            amount = float(input("Enter the amount to charge: "))
            if amount > 0:
                credit_card_number, credit_limit, spend_limit, due = database.get_credit_card(user.uid)
                if credit_card_number:
                    if due + amount > credit_limit:
                        print("Exceeded credit limit.")
                    elif amount > spend_limit:
                        print("Exceeded spend limit.")
                    else:
                        new_credit_due = due + amount
                        success = database.update_credit_card_due(user.uid, new_credit_due)
                        if success:
                            print(f"Charged {amount} to Credit Card {credit_card_number}.")
                        else:
                            print("Failed to update credit card due.")
                else:
                    print("Credit card details not found for the user.")
            else:
                print("Invalid amount for charge.")


        elif credit_choice == 3:
            card_number, credit_limit, spend_limit, due = database.get_credit_card(user.uid)
            if card_number:
                print("Card Number:", card_number)
                print("Credit Limit:", credit_limit)
                print("Spend Limit:", spend_limit)
                print("Current Due:", due)
            else:
                print("Credit card details not found for the user.")


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