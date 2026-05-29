
from utils.file_handler import load_json, save_json
from structures.hash_table import LoginHashTable

USER_FILE = "data/users.json"


def proses_login():
    login = LoginHashTable()

    login.load_users(USER_FILE)

    data = load_json(USER_FILE)

    username = input("Username : ")
    password = input("Password : ")

    if not login.login(username, password):
        print("Username atau password salah")
        return

    if username == data["admin"]["username"]:
        user = data["admin"]
        role = "admin"
        print("selamat datang admin!!")
        return user, role


    else:
        user = data["users"][username]
        role = "user"

    print("Login berhasil")

    return user, role

def proses_register():
    data = load_json(USER_FILE)

    print("\n=== REGISTER ===")

    username = input("Username : ").strip()

    # cek username sudah ada atau belum
    if username in data["users"]:
        print("Username sudah dipakai")
        return

    nama = input("Nama : ")
    email = input("Email : ")
    password = input("Password : ")

    if len(password) < 6:
        print("Password minimal 6 karakter")
        return

    konfirmasi = input("Konfirmasi Password : ")

    if password != konfirmasi:
        print("Password tidak cocok")
        return

    user_baru = {
        "username": username,
        "password": password,
        "nama": nama,
        "email": email,
        "saldo": 0,
        "poin": 0,
        "membership": "Bronze",
        "booking_history": [],
        "wishlist": []
    }

    data["users"][username] = user_baru

    save_json(USER_FILE, data)

    print("Register berhasil")

proses_register()