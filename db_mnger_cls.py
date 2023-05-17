import pymysql
import random

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='your_username',
            password='loliwonttellmypasslmfao',
            database='class12'
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def insert_user(self, email, password):
        query = "INSERT INTO credentials (uid, email, password) VALUES (%s, %s, %s)"
        uid = random.randint(1000000000, 9999999999)
        values = (uid, email, password)
        self.cursor.execute(query, values)
        self.connection.commit()
        return uid

    def insert_account(self, uid, account_number, withdraw_limit, balance):
        query = "INSERT INTO accounts (uid, accountno, withdrawlimit, balance) VALUES (%s, %s, %s, %s)"
        values = (uid, account_number, withdraw_limit, balance)
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
