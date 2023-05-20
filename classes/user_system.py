import random


class User:
    def __init__(self, email, password, uid=random.randint(1000000000, 9999999999)):
        self.uid = uid
        self.email = email
        self.password = password