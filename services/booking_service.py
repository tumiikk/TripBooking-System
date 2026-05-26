import csv
from utils.file_handler import load_json, save_json

FLIGHT_FILE = "data/flights.csv"
BOOKING_FILE = "data/bookings.json"
USER_FILE = "data/users.json"

def book_ticket(username):
    users = load_json(USER_FILE)

    if username not in users:
        print("User tidak ditemukan")
        return

    kode = input("Masukkan kode penerbangan: ")

    flights = []

    with open(FLIGHT_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            flights.append(row)

    selected = None

    for flight in flights:
        if flight["kode"] == kode:
            selected = flight
            break

    if not selected:
        print("Penerbangan tidak ditemukan")
        return

    harga = int(selected["harga"])

    if users[username]["saldo"] < harga:
        print("Saldo tidak cukup")
        return
    
    
    users[username]["saldo"] -= harga
    save_json(USER_FILE, users)

    bookings = load_json(BOOKING_FILE)

    bookings.append({
        "username": username,
        "kode": kode,
        "tujuan": selected["tujuan"],
        "harga": harga
    })

    save_json(BOOKING_FILE, bookings)

    print("Booking berhasil")
