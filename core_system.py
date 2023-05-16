import credit_system as c
import liability_system as l
import os

account1 = l.BankAccount("12345678", 1000)
account2 = l.BankAccount("87654321", 5000)
credit_card1 = c.CreditCard("1111-2222-3333-4444", 2000)
credit_card2 = c.CreditCard("5555-6666-7777-8888", 500)

accounts = [account1, account2]
credit_cards = [credit_card1, credit_card2]


def create_account(accounts):
    account_number = input("Enter the account number: ")
    existing_account_numbers = [account.account_number for account in accounts]

    if account_number in existing_account_numbers:
        print("Account number already exists.")
    else:
        initial_balance = float(input("Enter the initial balance: "))
        new_account = l.BankAccount(account_number, initial_balance)
        accounts.append(new_account)
        print(f"Account {account_number} created successfully.")


def create_credit_card(credit_cards):
    card_number = input("Enter the credit card number: ")
    existing_card_numbers = [card.card_number for card in credit_cards]

    if card_number in existing_card_numbers:
        print("Credit card number already exists.")
    else:
        credit_limit = float(input("Enter the credit limit: "))
        new_card = c.CreditCard(card_number, credit_limit)
        credit_cards.append(new_card)
        print(f"Credit Card {card_number} created successfully.")


def display_menu():
    print("\n==== Banking System ====")
    print("1. Select Account")
    print("2. Select Credit Card")
    print("3. Create New Account")
    print("4. Create New Credit Card Service")
    print("0. Exit")


def select_account(accounts):
    print("\n==== Select Account ====")
    for i, account in enumerate(accounts):
        print(f"{i + 1}. Account {account.account_number}")
    print("0. Back")

    choice = int(input("Enter your choice: "))
    if 0 <= choice <= len(accounts):
        return accounts[choice - 1] if choice != 0 else None
    else:
        print("Invalid choice.")
        return None


def select_credit_card(credit_cards):
    print("\n==== Select Credit Card ====")
    for i, card in enumerate(credit_cards):
        print(f"{i + 1}. Credit Card {card.card_number}")
    print("0. Back")

    choice = int(input("Enter your choice: "))
    if 0 <= choice <= len(credit_cards):
        return credit_cards[choice - 1] if choice != 0 else None
    else:
        print("Invalid choice.")
        return None


while True:
    os.system('cls')
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Exiting the program. Goodbye!")
        break
    elif choice == 1:
        selected_account = select_account(accounts)
        if selected_account:
            while True:
                print("\n==== Account Options ====")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("0. Back")

                account_choice = int(input("Enter your choice: "))

                if account_choice == 0:
                    break
                elif account_choice == 1:
                    amount = float(input("Enter the deposit amount: "))
                    selected_account.deposit(amount)
                elif account_choice == 2:
                    amount = float(input("Enter the withdrawal amount: "))
                    selected_account.withdraw(amount)
                elif account_choice == 3:
                    selected_account.print_balance()
                else:
                    print("Invalid choice.")
    elif choice == 2:
        selected_card = select_credit_card(credit_cards)
        if selected_card:
            while True:
                print("\n==== Credit Card Options ====")
                print("1. Charge")
                print("2. Pay")
                print("3. Check Balance")
                print("0. Back")

                card_choice = (input("Enter your choice: "))
                card_choice = int(card_choice)
                if card_choice == 0:
                    break
                elif card_choice == 1:
                    amount = float(input("Enter the charge amount: "))
                    selected_card.charge(amount)
                elif card_choice == 2:
                    amount = float(input("Enter the payment amount: "))
                    selected_card.pay(amount)
                elif card_choice == 3:
                    selected_card.print_balance()
                else:
                    print("Invalid choice.")
    elif choice == 3:
        create_account(accounts)
    elif choice == 4:
        create_credit_card(credit_cards)
    else:
        print("Invalid choice.")