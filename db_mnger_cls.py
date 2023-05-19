import pymysql
import random
import project_secrets


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user=project_secrets.databaseSecrets["user"],
            password=project_secrets.databaseSecrets["password"],
            database=project_secrets.databaseSecrets["database"]
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    # User Functions

    def insert_user(self, email, password):
        # Check if user with the same email already exists
        query = "SELECT uid FROM credentials WHERE email=%s"
        values = (email,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            return None, "User with the same email already exists."

        # Insert new user
        query = "INSERT INTO credentials (uid, email, password) VALUES (%s, %s, %s)"
        uid = random.randint(100, 999)
        values = (uid, email, password)
        self.cursor.execute(query, values)
        self.connection.commit()
        return uid, ""

    def get_user(self, email, password):
        # Check if email and password match
        query = "SELECT uid FROM credentials WHERE email=%s AND password=%s"
        values = (email, password)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            uid = result[0]
            return uid, ""
        else:
            # Check if email exists
            query = "SELECT uid FROM credentials WHERE email=%s"
            values = (email,)
            self.cursor.execute(query, values)
            result = self.cursor.fetchone()
            if result:
                return None, "Incorrect credentials."
            else:
                return None, "Provided email was not found in the registered accounts."

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
