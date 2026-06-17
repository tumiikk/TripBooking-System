from utils.json_handler import load_json, save_json
from structures.sorting import quick_sort_flights
from structures.linked_list import (SingleLinkedList,DoubleLinkedList,CircularLinkedList)
from structures.graph import Graph
from structures.tree import TreeNode, print_tree
from utils.search import linear_search, insert, range_search


FLIGHT_FILE = "data/flights.json"
BOOKING_FILE = "data/bookings.json"
DEST_FILE = "data/destination.json"
USER_FILE = "data/users.json"

class TravelService:
    def __init__(self, user):
        self.user = user
        self.rekomendasi = CircularLinkedList()
        self.current_rekomendasi = None
        self.booking_history = SingleLinkedList()

    

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

    def tampil_rekomendasi(self):
        if not self.rekomendasi.head:
            data = load_json(DEST_FILE)

            for kategori in data:
                for destinasi in data[kategori]:
                    self.rekomendasi.append(
                        f"{kategori} - {destinasi}"
                    )

            self.current_rekomendasi = self.rekomendasi.head

        print("REKOMENDASI DESTINASI HARI INI".center(40))
        print(self.current_rekomendasi.data.center(40))
        print("=" * 40)
        
        self.current_rekomendasi = self.current_rekomendasi.next


    def destinasi_populer(self):
        data = load_json(DEST_FILE)

        print("\n=== PILIH KATEGORI ===")
        kategori_list = list(data.keys())

        for i, kategori in enumerate(kategori_list, 1):
            print(f"{i}. {kategori}")

        pilih = int(input("Pilih kategori : ")) - 1
        kategori = kategori_list[pilih]

        dll = DoubleLinkedList()

        for destinasi in data[kategori]:
            dll.append(destinasi)

        current = dll.head

        while True:
            print("\n=== DESTINASI POPULER ===")
            print("Kategori  :", kategori)
            print("Destinasi :", current.data)

            print("\n1. Next")
            print("2. Prev")
            print("3. Keluar")

            menu = input("Pilih : ")

            if menu == "1":
                if current.next:
                    current = current.next
                else:
                    print("Sudah di destinasi terakhir!")

            elif menu == "2":
                if current.prev:
                    current = current.prev
                else:
                    print("Sudah di destinasi pertama!")

            elif menu == "3":
                break

    def lihat_seluruh_penerbangan(self):
        flights = load_json(FLIGHT_FILE)

        print("\n=== LIHAT PENERBANGAN ===")
        print("1. Urutkan dari termurah (Quick Sort)")
        print("2. Tanpa pengurutan")

        pilihan = input("Pilih : ")

        if pilihan == "1":
            flights = quick_sort_flights(flights)

        print("\n=== DAFTAR PENERBANGAN ===")

        print(
            f"{'No':<4}"
            f"{'Kode':<12}"
            f"{'Pesawat':<25}"
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
                f"{flight['nama_pesawat']:<25}"
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

            # Tuple (asal, tujuan)
            rute_penerbangan = (
                flight["asal"],
                flight["tujuan"]
            )

            graph.add_edge(
                rute_penerbangan[0],
                rute_penerbangan[1]
            )

        rute = graph.cari_rute(
            asal_transit,
            tujuan_transit
        )

        if rute:
            print("\nRute ditemukan:")
            print(" -> ".join(rute))
        else:
            print("\nRute transit tidak tersedia")
            
    
    def booking(self):
        from datetime import datetime

        flights = load_json(FLIGHT_FILE)

        self.lihat_seluruh_penerbangan()

        kode = input("Masukkan kode penerbangan : ").upper()

        # Ambil semua kode penerbangan
        kode_penerbangan = []
        for flight in flights:
            kode_penerbangan.append(flight["kode_penerbangan"])

        # Linear Search
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

        # Kurangi kursi
        flight["seat"] -= 1

        # Kurangi saldo user
        users = load_json(USER_FILE)

        for user in users:
            if user["username"] == self.user["username"]:
                user["saldo"] -= flight["harga"]
                self.user["saldo"] = user["saldo"]
                break

        # Simpan perubahan kursi dan saldo
        save_json(FLIGHT_FILE, flights)
        save_json(USER_FILE, users)

        # Buat data booking
        booking = {
            "username": self.user["username"],
            "kode_penerbangan": flight["kode_penerbangan"],
            "tanggal_penerbangan": flight["tanggal"],
            "asal": flight["asal"],
            "tujuan": flight["tujuan"],
            "harga": flight["harga"],
            "tanggal_booking": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }

        # Simpan ke bookings.json
        bookings = load_json(BOOKING_FILE)
        bookings.append(booking)
        save_json(BOOKING_FILE, bookings)

        # Simpan ke history linked list
        self.booking_history.append(booking)

        print("\nBooking berhasil!")
        print(
            f'{flight["asal"]} -> {flight["tujuan"]} | '
            f'Rp {flight["harga"]:,}'.replace(",", ".")
        )

    def lihat_riwayat_booking(self):
        self.booking_history.display_riwayat_booking()
        
    def cari_range_harga(self):
        low = int(input("Harga minimum : "))
        high = int(input("Harga maksimum : "))

        flights = load_json(FLIGHT_FILE)

        root = None

        for flight in flights:
            root = insert(root, flight["harga"], flight)

        hasil = range_search(root, low, high)

        if not hasil:
            print(
                f"\nTidak ada penerbangan dengan range harga "
                f"Rp {low:,}".replace(",", "."),
                "sampai",
                f"Rp {high:,}".replace(",", ".")
            )
            return

        print("\nHasil")

        for flight in hasil:
            print(
                flight["asal"],
                "->",
                flight["tujuan"],
                "| Rp",
                f'{flight["harga"]:,}'.replace(",", ".")
            )