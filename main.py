from services.auth_service import login, register
from services.flight_service import show_flights
from services.booking_service import book_ticket
from utils.file_handler import load_json

def main():
    while True:
        print("\n=== AEROBOOK ===")
        print("1. Register")
        print("2. Login")
        print("3. Lihat Penerbangan")
        print("4. Booking Tiket")
        print("5. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            register()

        elif pilih == "2":
            login()

        elif pilih == "3":
            show_flights()

        elif pilih == "4":
            username = input("Username: ")
            book_ticket(username)

        elif pilih == "5":
            print("Terima kasih telah menggunakan AeroBook")
            break

        else:
            print("Menu tidak valid")

if __name__ == "__main__":
    main()
