import random


class User:
    def __init__(self, email, password, uid=random.randint(100, 999)):
        self.uid = uid
        self.email = email
        self.password = password