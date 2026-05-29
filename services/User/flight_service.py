from utils.file_handler import load_json, save_json
from structures.graph import Graph
# def choose_flight():
#     asal = input(" asal :")
#     tujuan = input (" tujuan :")
#     return[asal,tujuan]

# FLIGHT_FILE = "data/flights.csv"
PAYMENT_FILE = "data/payment.json"

# def show_flights():
#     print("\n=== DAFTAR PENERBANGAN ===")

#     asal = input("asal : ")
#     tujuan = input("tujuan : ")

#     with open(FLIGHT_FILE, newline="", encoding="utf-8") as file:
#         reader = csv.DictReader(file)

#         for row in reader:
#             if row["asal"].lower() == asal.lower() and row["tujuan"].lower() == tujuan.lower() :

#                 print(f'''
#         Kode    : {row["kode"]}
#         Asal    : {row["asal"]}
#         Tujuan  : {row["tujuan"]}
#         Tanggal : {row["tanggal"]}
#         Harga   : Rp{row["harga"]}
#         Kursi   : {row["kursi"]}
#         ------------------------
#                 ''')

graph = Graph()
class FlightManager:

    def __init__(self, graph):
        self._graph = graph

    def cari_penerbangan(self):

        print("\n=== CARI PENERBANGAN ===")

        asal = input("Asal : ").title()
        tujuan = input("Tujuan : ").title()

        data = load_json(PAYMENT_FILE)

        flights = data["flights"]

        hasil = []

        # Linear Search
        for flight in flights.values():

            if (
                flight["asal"] == asal and
                flight["tujuan"] == tujuan and
                flight["kursi_tersedia"] > 0
            ):

                hasil.append(flight)

        # tidak ada flight
        if not hasil:

            print("Tidak ada penerbangan langsung.")

            rute = self._graph.bfs(asal, tujuan)

            if rute:
                print("Transit :", " -> ".join(rute))

            return []

        # output
        for i, f in enumerate(hasil, 1):

            print(f"""
            {i}. {f['kode']}
            {f['maskapai']}
            {f['asal']} -> {f['tujuan']}
            Rp{f['harga']:,}
    """)

        return hasil


    def pilih_kursi(self, flight):
        kursi = []

        for baris in range(1, 6):
            for kolom in ["A", "B", "C", "D"]:
                kursi.append(f"{baris}{kolom}")
        print("\n=== DAFTAR KURSI ===")
        for k in kursi:
            print(k, end="  ")
        while True:
            pilih = input("\nPilih kursi: ").upper()
            if pilih in kursi:
                print(f"Kursi {pilih} berhasil dipilih.")
                return pilih
            print("Kursi tidak valid.")

    def tiket_termurah(self):

        data = load_json(PAYMENT_FILE)

        flights = list(data["flights"].values())

        if not flights:
            print("Data kosong.")
            return

        # Minimum Search
        termurah = min(
            flights,
            key=lambda x: x["harga"]
        )

        print("\n=== TIKET TERMURAH ===")

        print(f"""
    Kode      : {termurah['kode']}
    Maskapai  : {termurah['maskapai']}
    Rute      : {termurah['asal']} -> {termurah['tujuan']}
    Harga     : Rp{termurah['harga']:,}
    """)

    def cari_range_harga(self):

        print("\n=== RANGE HARGA ===")

        min_harga = int(input("Harga minimum: "))
        max_harga = int(input("Harga maksimum: "))

        data = load_json(PAYMENT_FILE)

        flights = list(data["flights"].values())

        hasil = []

        # Linear Search
        for f in flights:

            if min_harga <= f["harga"] <= max_harga:

                hasil.append(f)

        if hasil:

            print("\n=== HASIL ===")

            for f in hasil:

                print(f"""
    {f['kode']} | {f['maskapai']}
    {f['asal']} -> {f['tujuan']}
    Rp{f['harga']:,}
    """)

        else:
            print("Tidak ada tiket.")


# terbang = FlightManager(graph)
# terbang.cari_penerbangan()

if __name__ == "__main__":

    graph = Graph()

    terbang = FlightManager(graph)

    print("""
=== TRIPBOOK ===
1. Booking Tiket
2. Tiket Termurah
3. Cari Range Harga
0. Keluar
""")

    pilih = input("Pilih menu: ")

    # =========================
    # BOOKING
    # =========================
    if pilih == "1":

        hasil = terbang.cari_penerbangan()

        # kalau ada hasil flight
        if hasil:

            nomor = int(
                input("\nPilih nomor flight: ")
            ) - 1

            flight = hasil[nomor]

            # pilih kursi
            kursi = terbang.pilih_kursi(flight)

            # output booking
            print(f"""
=== BOOKING BERHASIL ===

Kode Flight : {flight['kode']}
Maskapai    : {flight['maskapai']}
Rute        : {flight['asal']} -> {flight['tujuan']}
Kursi       : {kursi}
Total       : Rp{flight['harga']:,}
""")

    # =========================
    # TIKET TERMURAH
    # =========================
    elif pilih == "2":

        terbang.tiket_termurah()

    # =========================
    # RANGE HARGA
    # =========================
    elif pilih == "3":

        terbang.cari_range_harga()

    # =========================
    # KELUAR
    # =========================
    elif pilih == "0":

        print("Program selesai.")