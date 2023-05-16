import os
import user_system as us

while True:
    os.system('cls')
    user = us.User(39408503985, "lala", "1234")
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")
    if user.login(email_input, password_input):
        user.bank_account.print_balance()
        user.credit_card.print_balance()
        print("Welcome!")
        os.system('PAUSE')
    else:
        print("Login failed.")
