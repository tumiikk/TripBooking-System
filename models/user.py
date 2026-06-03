class User:
    def __init__(self, username, password, saldo=0):
        self.username = username
        self.password = password
        self.saldo = saldo
        self.wishlist = []

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "saldo": self.saldo,
            "wishlist": self.wishlist
        }
    
    