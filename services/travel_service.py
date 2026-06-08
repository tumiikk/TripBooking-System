from utils.json_handler import load_json, save_json
from structures.sorting import quick_sort
from structures.bst import insert, range_search
from structures.stack_queue import Stack
from structures.linked_list import (SingleLinkedList,DoubleLinkedList,CircularLinkedList)
from structures.graph import Graph
from structures.tree import TreeNode, print_tree
from utils.search import linear_search, binary_search
from datetime import datetime

FLIGHT_FILE = "data/flights.json"
BOOKING_FILE = "data/bookings.json"
DEST_FILE = "data/destination.json"

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

    def rekomendasi_destinasi(self):
        data = load_json(DEST_FILE)

        print("\n=== REKOMENDASI DESTINASI ===")

        root = TreeNode("Destinasi")

        for kategori, destinasi in data.items():
            kategori_node = TreeNode(kategori)

            for item in destinasi:
                kategori_node.add_child(TreeNode(item))

            root.add_child(kategori_node)

        print_tree(root)
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

        hasil = []

        for flight in flights:
            if (
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
        }

        bookings = load_json(BOOKING_FILE)
        bookings.append(booking)

        save_json(BOOKING_FILE, bookings)

        # self.queue.enqueue(booking)
        # self.stack.push("Booking tiket")

        self.booking_history.append(
            f'{flight["asal"]} -> {flight["tujuan"]}'
        )

        print("Booking berhasil.")

    def lihat_riwayat_booking(self):
        self.booking_history.display()
        
    def cari_range_harga(self):
        low = int(input("Harga minimum : "))
        high = int(input("Harga maksimum : "))

        flights = load_json(FLIGHT_FILE)

        root = None

        for flight in flights:
            root = insert(root, flight["harga"], flight)

        hasil = range_search(root, low, high)

        print("\nHasil")

        for flight in hasil:
            print(
                flight["asal"],
                "->",
                flight["tujuan"],
                "| Rp",
                flight["harga"]
            )