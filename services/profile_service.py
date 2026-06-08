from utils.json_handler import load_json, save_json
<<<<<<< HEAD
from structures.stack_queue import Stack
# from models.user import User 

USER_FILE = "data/users.json"
BOOKING_FILE = "data/bookings.json"
FLIGHT_FILE = "data/flights.json"
=======

USER_FILE = "data/users.json"
BOOKING_FILE = "data/bookings.json"

>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde

class ProfileService:
    def __init__(self, user):
        self.user = user

    def lihat_profil(self):
        print("\n=== PROFIL ===")
        print("Username :", self.user["username"])

    def lihat_saldo(self):
        print("Saldo :", self.user["saldo"])

    def isi_saldo(self):
        jumlah = int(input("Nominal : "))

        users = load_json(USER_FILE)

        for user in users:
            if user["username"] == self.user["username"]:
                user["saldo"] += jumlah
                self.user["saldo"] = user["saldo"]

        save_json(USER_FILE, users)

        print("Saldo berhasil ditambah.")

    def tambah_wishlist(self):
        tujuan = input("Destinasi : ")

        wishlist = set(self.user["wishlist"])
        wishlist.add(tujuan)

        self.user["wishlist"] = list(wishlist)

        users = load_json(USER_FILE)

        for user in users:
            if user["username"] == self.user["username"]:
                user["wishlist"] = self.user["wishlist"]

        save_json(USER_FILE, users)

        print("Wishlist ditambahkan.")

    def lihat_wishlist(self):
        print("\nWishlist")

        for item in self.user["wishlist"]:
            print("-", item)
<<<<<<< HEAD
    
    
    def hapus_wishlist(self):
        tujuan = input("Destinasi : ")

        wishlist = set(self.user["wishlist"])
        wishlist.pop(tujuan)

        self.user["wishlist"] = list(wishlist)

        users = load_json(USER_FILE)

        for user in users:
            if user["username"] == self.user["username"]:
                user["wishlist"] = self.user["wishlist"]

        save_json(USER_FILE, users)

        print("Wishlist ditambahkan.")

    def lihat_riwayat_booking(self):
        bookings = load_json(BOOKING_FILE)
        booking_user = []
=======

    def riwayat_booking(self):
        bookings = load_json(BOOKING_FILE)

>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde
        print("\nRiwayat Booking")

        for booking in bookings:
            if booking["username"] == self.user["username"]:
<<<<<<< HEAD
                
                print(f"kode_penerbangan :  {booking["kode_penerbangan"]}")
                print(f"kota asal :  {booking["asal"]}")
                print(f"kota tujuann :  {booking["tujuan"]}")
                print(f"harga tiket :  {booking["harga"]}")
                print(f"tanggal booking :  {booking["tanggal_booking"]}")
                print("")
                

    def undo_booking_terakhir(self):
        bookings = load_json(BOOKING_FILE)

        stack = Stack()

        # Masukkan semua booking user ke stack
        for booking in bookings:
            if booking["username"] == self.user["username"]:
                stack.push(booking)

        if len(stack.show()) == 0:
            print("Tidak ada booking yang bisa di-undo.")
            return

        booking_terakhir = stack.pop()

        flights = load_json(FLIGHT_FILE)
        users = load_json(USER_FILE)

        # Hapus booking terakhir dari bookings.json
        for i in range(len(bookings) - 1, -1, -1):
            if (
                bookings[i]["username"] == booking_terakhir["username"]
                and
                bookings[i]["kode_penerbangan"] == booking_terakhir["kode_penerbangan"]
                and
                bookings[i]["tanggal_booking"] == booking_terakhir["tanggal_booking"]
            ):
                bookings.pop(i)
                break

        # Kembalikan kursi
        for flight in flights:
            if flight["kode_penerbangan"] == booking_terakhir["kode_penerbangan"]:
                flight["seat"] += 1
                break

        # Kembalikan saldo
        for user in users:
            if user["username"] == booking_terakhir["username"]:
                user["saldo"] += booking_terakhir["harga"]
                self.user["saldo"] = user["saldo"]
                break

        save_json(BOOKING_FILE, bookings)
        save_json(FLIGHT_FILE, flights)
        save_json(USER_FILE, users)

        print("Booking terakhir berhasil dibatalkan.")
=======
                print(
                    booking["origin"],
                    "->",
                    booking["destination"],
                    "| Rp",
                    booking["price"]
                )
>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde
