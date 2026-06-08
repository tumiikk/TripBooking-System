from services.auth_service import AuthService
from services.profile_service import ProfileService
from services.travel_service import TravelService


def profile_menu(user):
    profile = ProfileService(user)
    travel = TravelService(user)
    while True:
        print("\n=== PROFILE CENTER ===")
        print("1. Lihat Profil")
        print("2. Lihat Saldo")
        print("3. Isi Saldo")
        print("4. Wishlist")
        print("5. Riwayat Booking")
        print("0. Kembali")

        pilih = input("Pilih : ")

        if pilih == "1":
            profile.lihat_profil()

        elif pilih == "2":
            profile.lihat_saldo()

        elif pilih == "3":
            profile.isi_saldo()

        elif pilih == "4":
            profile.lihat_wishlist()
            tambah = input("\n Mau tambah wishlist?? (y/n)").lower()
            if tambah == "y":
                profile.tambah_wishlist()
                continue
            print("baiklah..")

        elif pilih == "5":
            print("pilihan lihat riwayat booking")
            print("1. seluruhnya")
            print("2. yang barusan")
            pilihan_riwayat = input("pilih : ")
            if pilihan_riwayat == "1":
                profile.lihat_riwayat_booking()
            elif pilihan_riwayat == "2":
                travel.lihat_riwayat_booking()

            undo = input("\n Mau undo book terakhir?? (y/n)").lower()

            if undo == "y" :
                profile.undo_booking_terakhir()
                continue
            print("baiklahh..")

        elif pilih == "0":
            break


def travel_menu(user):
    travel = TravelService(user)

    while True:
        print("\n=== TRAVEL CENTER ===")
        print("1. Rekomendasi Destinasi")
        print("2. Destinasi Populer")
        print("3. Lihat Penerbangan")
        print("4. Booking Penerbangan")
        print("5. menu search")

        print("0. Kembali")

        pilih = input("Pilih : ")

        if pilih == "1":
            travel.rekomendasi_destinasi()

        elif pilih == "2":
            travel.destinasi_populer()

        elif pilih == "3":
            print("pilih metode lihat penerbangannya")
            print("1. lihat seluruh penerbangan")
            print("2. lihat rute ke kota tertentu")
            print("3. lihat penerbangan sesuai budget")

            pilihan = input("pilihan : ")
            if pilihan == "1" :
                travel.lihat_seluruh_penerbangan()
            elif pilihan == "2":
                travel.lihat_rute_penerbangan_langsung()
            elif pilihan == "3":
                travel.cari_range_harga()

        elif pilih == "4":
            travel.booking()

        elif pilih == "5":
            travel.menu_searching()
            
        elif pilih == "0":  
            break


def main():
    auth = AuthService()

    while True:
        print("\n=== AEROBOOK ===")
        print("1. Register")
        print("2. Login")
        print("0. Keluar")

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

                    elif menu == "0":
                        break

        elif pilih == "3":
            print("Terima kasih.")
            break

main()