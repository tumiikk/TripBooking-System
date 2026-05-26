import csv

# def choose_flight():
#     asal = input(" asal :")
#     tujuan = input (" tujuan :")
#     return[asal,tujuan]

FLIGHT_FILE = "data/flights.csv"

def show_flights():
    print("\n=== DAFTAR PENERBANGAN ===")

    asal = input("asal : ")
    tujuan = input("tujuan : ")

    with open(FLIGHT_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["asal"].lower() == asal.lower() and row["tujuan"].lower() == tujuan.lower() :

                print(f'''
        Kode    : {row["kode"]}
        Asal    : {row["asal"]}
        Tujuan  : {row["tujuan"]}
        Tanggal : {row["tanggal"]}
        Harga   : Rp{row["harga"]}
        Kursi   : {row["kursi"]}
        ------------------------
                ''')
        
            
                
