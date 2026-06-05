from utils.json_handler import load_json, save_json

USER_FILE = "data/users.json"
BOOKING_FILE = "data/bookings.json"


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

    def riwayat_booking(self):
        bookings = load_json(BOOKING_FILE)

        print("\nRiwayat Booking")

        for booking in bookings:
            if booking["username"] == self.user["username"]:
                print(
                    booking["origin"],
                    "->",
                    booking["destination"],
                    "| Rp",
                    booking["price"]
                )