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
    # username
        while True:
            username = input("Username : ")

            if self.table.search(username):
                print("Username sudah ada.")
            else:
                break

        # email
        while True:
            try:
                email = input("Email : ")

                if "@" not in email:
                    raise ValueError("Email harus mengandung '@'.")

                break

            except ValueError as e:
                print("Error:", e)

        # password
        while True:
            try:
                password = input("Password : ")

                if len(password) < 4:
                    raise ValueError("Password harus lebih dari 4 karakter.")

                break

            except ValueError as e:
                print("Error:", e)

        user = {
            "username": username,
            "email": email,
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