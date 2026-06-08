from utils.json_handler import load_json, save_json
from structures.sorting import quick_sort
from structures.bst import insert, range_search
<<<<<<< HEAD
from structures.stack_queue import Stack
from structures.linked_list import (SingleLinkedList,DoubleLinkedList,CircularLinkedList)
from structures.graph import Graph
from structures.tree import TreeNode, print_tree
from utils.search import linear_search, binary_search
from datetime import datetime
=======
from structures.stack_queue import Stack, Queue
from structures.linked_list import CircularLinkedList
>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde

FLIGHT_FILE = "data/flights.json"
BOOKING_FILE = "data/bookings.json"
DEST_FILE = "data/destination.json"

<<<<<<< HEAD
class TravelService:
    def __init__(self, user):
        self.user = user
        self.booking_history = SingleLinkedList()

    # def rekomendasi_destinasi(self):
    #     data = load_json(DEST_FILE)

    #     print("\n=== REKOMENDASI DESTINASI ===")

    #     for kategori, destinasi in data.items():
    #         print(f"\n{kategori}")

    #         for item in destinasi:
    #             print("-", item)
=======

class TravelService:
    def __init__(self, user):
        self.user = user

        self.stack = Stack()
        self.queue = Queue()
>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde

    def rekomendasi_destinasi(self):
        data = load_json(DEST_FILE)

        print("\n=== REKOMENDASI DESTINASI ===")

<<<<<<< HEAD
        root = TreeNode("Destinasi")

        for kategori, destinasi in data.items():
            kategori_node = TreeNode(kategori)

            for item in destinasi:
                kategori_node.add_child(TreeNode(item))

            root.add_child(kategori_node)

        print_tree(root)
    def destinasi_populer(self):
        data = load_json(DEST_FILE)
=======
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

>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde
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

<<<<<<< HEAD

    def lihat_seluruh_penerbangan(self):
        flights = load_json(FLIGHT_FILE)

        print("\n=== LIHAT PENERBANGAN ===")
        print("1. Urutkan dari termurah")
        print("2. Tanpa pengurutan")

        pilihan = input("Pilih : ")

        if pilihan == "1":
            flights = sorted(flights, key=lambda x: x["harga"])

        print("\n=== DAFTAR PENERBANGAN ===")

        print(
            f"{'No':<4}"
            f"{'Kode':<12}"
            f"{'Pesawat':<20}"
            f"{'Asal':<15}"
            f"{'Tujuan':<15}"
            f"{'Harga':<12}"
            f"{'Tanggal':<15}"
            f"{'Seat':<6}"
        )

        print("-" * 100)

        for i, flight in enumerate(flights, 1):
            print(
                f"{i:<4}"
                f"{flight['kode_penerbangan']:<12}"
                f"{flight['nama_pesawat']:<20}"
                f"{flight['asal']:<15}"
                f"{flight['tujuan']:<15}"
                f"{flight['harga']:<12}"
                f"{flight['tanggal']:<15}"
                f"{flight['seat']:<6}"
            )


    def lihat_rute_penerbangan_langsung(self):
        flights = load_json(FLIGHT_FILE)

        asal = input("Masukkan kota asal : ").title()
        tujuan = input("Masukkan kota tujuan : ").title()

=======
    def lihat_penerbangan(self):
        asal = input("Kota asal : ")
        tujuan = input("Kota tujuan : ")

        flights = load_json(FLIGHT_FILE)

>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde
        hasil = []

        for flight in flights:
            if (
<<<<<<< HEAD
                flight["asal"].title() == asal
                and
                flight["tujuan"].title() == tujuan
            ):
                hasil.append(flight)

        if not hasil:
            print("Penerbangan tidak ditemukan.")
            print("kita bakal liat rute transitnya :) ")
            enter = input("tekan enter buat lanjut..")
            self.lihat_rute_penerbangan_transit(asal, tujuan)
            return


        print("\n=== HASIL PENCARIAN ===")

        print(
            f"{'No':<4}"
            f"{'Kode':<12}"
            f"{'Pesawat':<20}"
            f"{'Asal':<15}"
            f"{'Tujuan':<15}"
            f"{'Harga':<12}"
            f"{'Tanggal':<15}"
            f"{'Seat':<6}"
        )

        print("-" * 100)

        for i, flight in enumerate(hasil, 1):
            print(
                f"{i:<4}"
                f"{flight['kode_penerbangan']:<12}"
                f"{flight['nama_pesawat']:<20}"
                f"{flight['asal']:<15}"
                f"{flight['tujuan']:<15}"
                f"{flight['harga']:<12}"
                f"{flight['tanggal']:<15}"
                f"{flight['seat']:<6}"
            )

    def lihat_rute_penerbangan_transit(self, asal_transit, tujuan_transit):
        flights = load_json(FLIGHT_FILE)
        graph = Graph()

        for flight in flights:
            graph.add_edge(
                flight["asal"],
                flight["tujuan"]
            )

        rute = graph.cari_rute(asal_transit, tujuan_transit)

        if rute:
            print("\nRute ditemukan:")
            print(" -> ".join(rute))
        else:
            print("\nRute transit tidak tersedia")

    def menu_searching(self):

        while True:

            print("\n=== SEARCHING ===")
            print("1. Linear Search (Tujuan)")
            print("2. Binary Search (Harga)")
            print("3. Kembali")

            pilih = input("Pilih : ")

            if pilih == "1":
                self.cari_tujuan()

            elif pilih == "2":
                self.cari_harga()

            elif pilih == "3":
                break
            
    from datetime import datetime

    def booking(self):
       
        flights = load_json(FLIGHT_FILE)

        print("\n=== DAFTAR PENERBANGAN ===")
        for flight in flights:
            print(
                flight["kode_penerbangan"],
                "|",
                flight["asal"],
                "->",
                flight["tujuan"],
                "| Rp",
                flight["harga"]
            )

        kode = input("Masukkan kode penerbangan : ")

        # Ambil semua kode penerbangan
        kode_penerbangan = []
        for flight in flights:
            kode_penerbangan.append(flight["kode_penerbangan"])

        # Pakai linear search
        index = linear_search(kode_penerbangan, kode)

        if index == -1:
            print("Kode penerbangan tidak ditemukan.")
            return
        
        flight = flights[index]

        if self.user["saldo"] < flight["harga"]:
            print("Saldo tidak cukup.")
            return

        if flight["seat"] < 1:
            print("Kursi sudah habis.")
            return
        
        flight["seat"] -= 1

        self.user["saldo"] -= flight["harga"]

        booking = {
            "username": self.user["username"],
            "kode_penerbangan": flight["kode_penerbangan"],
            "tanggal_penerbangan": flight["tanggal"],
            "asal": flight["asal"],
            "tujuan": flight["tujuan"],
            "harga": flight["harga"],
            "tanggal_booking": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
=======
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
>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde
        }

        bookings = load_json(BOOKING_FILE)
        bookings.append(booking)

        save_json(BOOKING_FILE, bookings)

<<<<<<< HEAD
        # self.queue.enqueue(booking)
        # self.stack.push("Booking tiket")

        self.booking_history.append(
            f'{flight["asal"]} -> {flight["tujuan"]}'
        )

        print("Booking berhasil.")

    def lihat_riwayat_booking(self):
        self.booking_history.display()
        
=======
        self.queue.enqueue(booking)
        self.stack.push("Booking tiket")

        print("Booking berhasil.")

>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde
    def cari_range_harga(self):
        low = int(input("Harga minimum : "))
        high = int(input("Harga maksimum : "))

        flights = load_json(FLIGHT_FILE)

        root = None

        for flight in flights:
<<<<<<< HEAD
            root = insert(root, flight["harga"], flight)
=======
            root = insert(root, flight["price"], flight)
>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde

        hasil = range_search(root, low, high)

        print("\nHasil")

        for flight in hasil:
            print(
<<<<<<< HEAD
                flight["asal"],
                "->",
                flight["tujuan"],
                "| Rp",
                flight["harga"]
=======
                flight["origin"],
                "->",
                flight["destination"],
                "| Rp",
                flight["price"]
>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde
            )