import pymysql
import random
import project_secrets


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password=project_secrets.secrectsDict["passworddb"],
            database='class12'
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def insert_user(self, email, password):
        query = "INSERT INTO credentials (uid, email, password) VALUES (%s, %s, %s)"
        uid = random.randint(100, 999)
        values = (uid, email, password)
        self.cursor.execute(query, values)
        self.connection.commit()
        return uid

    def insert_account(self, uid, withdraw_limit, balance):
        query = "INSERT INTO accounts (uid, accountno, withdrawlimit, balance) VALUES (%s, %s, %s, %s)"
        values = (uid, random.randint(100, 999), withdraw_limit, balance)
        self.cursor.execute(query, values)
        self.connection.commit()

    def insert_credit_card(self, uid, credit_limit, spend_limit, due):
        query = "INSERT INTO creditcard (uid, cardnum, creditlimit, spendlimit, due) VALUES (%s, %s, %s, %s, %s)"
        values = (uid, random.randint(100, 999),
                  credit_limit, spend_limit, due)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_user(self, email, password):
        query = "SELECT uid FROM credentials WHERE email=%s AND password=%s"
        values = (email, password)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            uid = result[0]
            return uid
        return None

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

    def get_credit_card(self, uid):
        query = "SELECT cardnum, creditlimit, due FROM creditcard WHERE uid=%s"
        values = (uid,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            card_number, credit_limit, balance = result
            return card_number, credit_limit, balance
        return None

    def update_credit_card_balance(self, uid, balance):
        query = "UPDATE creditcard SET due=%s WHERE uid=%s"
        values = (balance, uid)
        self.cursor.execute(query, values)
        self.connection.commit()
