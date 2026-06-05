from utils.json_handler import load_json, save_json
from structures.sorting import quick_sort
from structures.bst import insert, range_search
from structures.stack_queue import Stack, Queue
from structures.linked_list import CircularLinkedList

FLIGHT_FILE = "data/flights.json"
BOOKING_FILE = "data/bookings.json"
DEST_FILE = "data/destination.json"


class TravelService:
    def __init__(self, user):
        self.user = user

        self.stack = Stack()
        self.queue = Queue()

    def rekomendasi_destinasi(self):
        data = load_json(DEST_FILE)

        print("\n=== REKOMENDASI DESTINASI ===")

        for kategori, destinasi in data.items():
            print(f"\n{kategori}")

            for item in destinasi:
                print("-", item)

    # def destinasi_populer(self):
    #     data = load_json(DEST_FILE)

    #     print("\nDestinasi Populer")

    #     for item in data["popular"]:
    #         print("-", item)

    def destinasi_populer(self):
        data = load_json(DEST_FILE)

        cll = CircularLinkedList()

        for kategori in data:
            for destinasi in data[kategori]:
                cll.append(destinasi)

        current = cll.head

        while True:
            print("\n=== DESTINASI POPULER ===")
            print("Destinasi :", current.data)

            print("\n1. Next")
            print("2. Prev")
            print("3. Keluar")

            pilih = input("Pilih : ")

            if pilih == "1":
                current = current.next

            elif pilih == "2":
                current = current.prev

            elif pilih == "3":
                break

    def lihat_penerbangan(self):
        asal = input("Kota asal : ")
        tujuan = input("Kota tujuan : ")

        flights = load_json(FLIGHT_FILE)

        hasil = []

        for flight in flights:
            if (
                flight["origin"].lower() == asal.lower()
                and
                flight["destination"].lower() == tujuan.lower()
            ):
                hasil.append(flight)

        hasil = quick_sort(hasil)

        print("\nDaftar Penerbangan")

        for i, flight in enumerate(hasil, 1):
            print(
                i,
                flight["origin"],
                "->",
                flight["destination"],
                "| Rp",
                flight["price"]
            )

    def booking(self):
        flights = load_json(FLIGHT_FILE)

        for i, flight in enumerate(flights, 1):
            print(
                i,
                flight["origin"],
                "->",
                flight["destination"],
                "| Rp",
                flight["price"]
            )

        pilih = int(input("Pilih nomor : ")) - 1

        flight = flights[pilih]

        if self.user["saldo"] < flight["price"]:
            print("Saldo tidak cukup.")
            return

        self.user["saldo"] -= flight["price"]

        booking = {
            "username": self.user["username"],
            "origin": flight["origin"],
            "destination": flight["destination"],
            "price": flight["price"]
        }

        bookings = load_json(BOOKING_FILE)
        bookings.append(booking)

        save_json(BOOKING_FILE, bookings)

        self.queue.enqueue(booking)
        self.stack.push("Booking tiket")

        print("Booking berhasil.")

    def cari_range_harga(self):
        low = int(input("Harga minimum : "))
        high = int(input("Harga maksimum : "))

        flights = load_json(FLIGHT_FILE)

        root = None

        for flight in flights:
            root = insert(root, flight["price"], flight)

        hasil = range_search(root, low, high)

        print("\nHasil")

        for flight in hasil:
            print(
                flight["origin"],
                "->",
                flight["destination"],
                "| Rp",
                flight["price"]
            )