from services.auth_service import AuthService
from services.profile_service import ProfileService
from services.travel_service import TravelService


def profile_menu(user):
    profile = ProfileService(user)

    while True:
        print("\n=== PROFILE CENTER ===")
        print("1. Lihat Profil")
        print("2. Lihat Saldo")
        print("3. Isi Saldo")
        print("4. Tambah Wishlist")
        print("5. Lihat Wishlist")
        print("6. Riwayat Booking")
        print("7. Kembali")

        pilih = input("Pilih : ")

        if pilih == "1":
            profile.lihat_profil()

        elif pilih == "2":
            profile.lihat_saldo()

        elif pilih == "3":
            profile.isi_saldo()

        elif pilih == "4":
            profile.tambah_wishlist()

        elif pilih == "5":
            profile.lihat_wishlist()

        elif pilih == "6":
            profile.riwayat_booking()

        elif pilih == "7":
            break


def travel_menu(user):
    travel = TravelService(user)

    while True:
        print("\n=== TRAVEL CENTER ===")
        print("1. Rekomendasi Destinasi")
        print("2. Destinasi Populer")
        print("3. Lihat Penerbangan")
        print("4. Booking Penerbangan")
        print("5. Cari Tiket Range Harga")
        print("6. Kembali")

        pilih = input("Pilih : ")

        if pilih == "1":
            travel.rekomendasi_destinasi()

        elif pilih == "2":
            travel.destinasi_populer()

        elif pilih == "3":
            travel.lihat_penerbangan()

        elif pilih == "4":
            travel.booking()

        elif pilih == "5":
            travel.cari_range_harga()

        elif pilih == "6":
            break


def main():
    auth = AuthService()

    while True:
        print("\n=== AEROBOOK ===")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")

        pilih = input("Pilih : ")

        if pilih == "1":
            auth.register()

        elif pilih == "2":
            user = auth.login()

            if user:
                while True:
                    print("\n=== MENU USER ===")
                    print("1. Profile Center")
                    print("2. Travel Center")
                    print("3. Logout")

                    menu = input("Pilih : ")

                    if menu == "1":
                        profile_menu(user)

                    elif menu == "2":
                        travel_menu(user)

                    elif menu == "3":
                        break

        elif pilih == "3":
            print("Terima kasih.")
            break


main()