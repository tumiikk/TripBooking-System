from utils.file_handler import load_json, save_json

USER_FILE = "data/users.json"

def register():
    users = load_json(USER_FILE)

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users:
        print("Username sudah ada")
        return

    users[username] = {
        "password": password,
        "saldo": 1000000
    }

    save_json(USER_FILE, users)
    print("Register berhasil")

def login():
    users = load_json(USER_FILE)

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login berhasil")
    else:
        print("Login gagal")


