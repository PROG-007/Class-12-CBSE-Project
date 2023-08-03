import pymysql
import random
from classes import project_secrets

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user=project_secrets.databaseSecrets["user"],
            password=project_secrets.databaseSecrets["password"],
            database=project_secrets.databaseSecrets["database"]
        )
        self.cursor = self.connection.cursor()
        self.create_database()
        self.insert_dummy_users(15)
        self.create_tables()

    def close(self):
        self.connection.close()

    # Setup Functions
    def create_database(self):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {project_secrets.databaseSecrets['database']}")

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS credentials (
                uid CHAR(9) PRIMARY KEY,
                email CHAR(100) UNIQUE,
                password CHAR(20)
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                uid CHAR(9) PRIMARY KEY,
                accountno INT,
                withdrawlimit INT,
                balance INT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS creditcard (
                uid CHAR(9) PRIMARY KEY,
                cardnum INT,
                creditlimit INT,
                spendlimit INT,
                due INT
            )
        ''')
    
    def insert_dummy_users(self, num_users):
            names = [
                "Alice", "Bob", "Charlie", "David", "Eve",
                "Fiona", "Grace", "Hector", "Isabel", "Jack"
            ]
            for _ in range(num_users):
                name = random.choice(names)
                uid = str(random.randint(100000000, 999999999))
                email = f"{name.lower()}@example.com"
                password = "password123"  # You should use a secure method to generate passwords
                self.insert_user(email, password)
                print(f"Inserted user: {name} (UID: {uid})")
    # User Functions

    def insert_user(self, email, password):
        # Check if user with the same email already exists
        query = "SELECT uid FROM credentials WHERE email=%s"
        values = (email,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            return None

        # Insert new user
        query = "INSERT INTO credentials (uid, email, password) VALUES (%s, %s, %s)"
        uid = random.randint(100, 999)
        values = (uid, email, password)
        self.cursor.execute(query, values)
        self.connection.commit()
        return uid

    def get_user(self, email, password):
        # Check if email and password match
        query = "SELECT uid FROM credentials WHERE email=%s AND password=%s"
        values = (email, password)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            uid = result[0]
            return uid
        return None
    # Account Functions

    def insert_account(self, uid, withdraw_limit, balance):
        query = "INSERT INTO accounts (uid, accountno, withdrawlimit, balance) VALUES (%s, %s, %s, %s)"
        values = (uid, random.randint(100, 999), withdraw_limit, balance)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_account(self, uid):
        query = "SELECT accountno, withdrawlimit, balance FROM accounts WHERE uid=%s"
        values = (uid,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            account_number, withdraw_limit, balance = result
            return account_number, withdraw_limit, balance
        return None

    def update_account_balance(self, uid, balance):
        query = "UPDATE accounts SET balance=%s WHERE uid=%s"
        values = (balance, uid)
        self.cursor.execute(query, values)
        self.connection.commit()

    def transfer_money(self, sender_uid, recipient_uid, amount):
        # Check if sender has sufficient balance
        sender_account = self.get_account(sender_uid)
        if sender_account:
            _, _, sender_balance = sender_account
            if sender_balance >= amount:
                # Update recipient's and sender's balance
                recipient_account = self.get_account(recipient_uid)
                if recipient_account:
                    _, _, recipient_balance = recipient_account
                    # Update recipient's balance
                    recipient_new_balance = recipient_balance + amount
                    self.update_account_balance(recipient_uid, recipient_new_balance)
                    
                    # Update sender's balance
                    sender_new_balance = sender_balance - amount
                    self.update_account_balance(sender_uid, sender_new_balance) 

                    return True
                else:
                    return "Recipient account not found."
            else:
                return "Insufficient balance."
        else:
            return "Sender account not found."


    # Credit Card Functions

    def insert_credit_card(self, uid, credit_limit, spend_limit):
        query = "INSERT INTO creditcard (uid, cardnum, creditlimit, spendlimit, due) VALUES (%s, %s, %s, %s, %s)"
        values = (uid, random.randint(100, 999), credit_limit, spend_limit, 0) 
        # credit_limit = 10000 by default as written in core_system.py
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_credit_card(self, uid):
        query = "SELECT cardnum, creditlimit, spendlimit, due FROM creditcard WHERE uid=%s"
        values = (uid,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            card_number, credit_limit, spend_limit, due = result
            return card_number, credit_limit, spend_limit, due
        return None

    def update_credit_card_due(self, uid, due):
        query = "UPDATE creditcard SET due=%s WHERE uid=%s"
        values = (due, uid)
        self.cursor.execute(query, values)
        self.connection.commit()
