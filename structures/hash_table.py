import json

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return

        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                return item[1]

        return None


class LoginHashTable(HashTable):
    def hash_password(self, password):
        return str(sum(ord(c) for c in password))

    def load_users(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)

        admin = data.get("admin")

        if admin:
            admin["password"] = self.hash_password(admin["password"])
            self.insert(admin["username"], admin)

        for username, user in data["users"].items():
            user["password"] = self.hash_password(user["password"])
            self.insert(username, user)

    def login(self, username, password):
        user = self.search(username)

        if not user:
            return False

        return user["password"] == self.hash_password(password)