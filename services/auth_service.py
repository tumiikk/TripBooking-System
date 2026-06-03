from structures.hash_table import HashTable
from utils.json_handler import load_json, save_json

USER_FILE = "data/users.json"


class AuthService:
    def __init__(self):
        self.users = load_json(USER_FILE)
        self.table = HashTable()

        for user in self.users:
            self.table.insert(user["username"], user)

    def register(self):
        username = input("Username : ")
        password = input("Password : ")

        if self.table.search(username):
            print("Username sudah ada.")
            return

        user = {
            "username": username,
            "password": password,
            "saldo": 0,
            "wishlist": []
        }

        self.users.append(user)
        save_json(USER_FILE, self.users)

        self.table.insert(username, user)

        print("Register berhasil.")

    def login(self):
        username = input("Username : ")
        password = input("Password : ")

        user = self.table.search(username)

        if user and user["password"] == password:
            print("Login berhasil.")
            return user

        print("Login gagal.")
        return None