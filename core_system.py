import os
import user_system as us

User = us.User

def print_auth_menu():
    print("1. Login")
    print("2. Create New Account")
    print("3. Exit")

def handle_login(users):
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")

    for user in users:
        if user.login(email_input, password_input):
            print("Welcome!")
            return user

    print("Login failed.")
    return None

def handle_signup(users):


    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")

    for user in users:
        if email_input == user.email:
            print("Email already exists. Please login.")
            return None
        
    new_user = User(email_input, password_input)
    users.append(new_user)

    print("Account created successfully.")
    print("Welcome!")
    return new_user

def print_main_menu():
    print("\nMain Menu:")
    print("1. Manage Bank Account")
    print("2. Manage Credit Card")
    print("3. Logout")

def handle_main_menu(user):
    while True:
        print_main_menu()
        account_choice = int(input("Enter your choice: "))

        if account_choice == 1:
            handle_bank_account_menu(user)
        elif account_choice == 2:
            handle_credit_card_menu(user)
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

def handle_bank_account_menu(user):
    while True:
        print_bank_account_menu()
        bank_choice = int(input("Enter your choice: "))

        if bank_choice == 1:
            amount = float(input("Enter the amount to withdraw: "))
            user.bank_account.withdraw(amount)
        elif bank_choice == 2:
            amount = float(input("Enter the amount to deposit: "))
            user.bank_account.deposit(amount)
        elif bank_choice == 3:
            user.bank_account.print_balance()
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

def handle_credit_card_menu(user):
    while True:
        print_credit_card_menu()
        credit_choice = int(input("Enter your choice: "))

        if credit_choice == 1:
            amount = float(input("Enter the amount to pay: "))
            user.credit_card.pay(amount)
        elif credit_choice == 2:
            amount = float(input("Enter the amount to charge: "))
            user.credit_card.charge(amount)
        elif credit_choice == 3:
            print("Total Due Bill:", user.credit_card.balance)
        elif credit_choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
        next()

users = [
    User("user1@example.com", "password1"),
    User("user2@example.com", "password2"),
]

def next():
    os.system('PAUSE')
    os.system('cls')

def cls():
    os.system('cls')

cls()

while True:
    print_auth_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        user = handle_login(users)
        if user is not None:
            handle_main_menu(user)

    elif choice == 2:
        new_user = handle_signup(users)
        if new_user is not None:
            handle_main_menu(new_user)

    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")
    next()