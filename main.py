from services.auth_service import AuthService
from services.profile_service import ProfileService
from services.travel_service import TravelService


def profile_menu(user):
    profile = ProfileService(user)


    while True:
        try:
            print("\n" + "=" * 40)
            print("👤 PROFILE CENTER".center(40))
            print("=" * 40)
            print("1. Lihat Profil")
            print("2. Lihat Saldo")
            print("3. Isi Saldo")
            print("4. Wishlist")
            print("0. Kembali")
            print("-" * 40)

            pilih = input("Pilih : ")

            if pilih == "1":
                profile.lihat_profil()

            elif pilih == "2":
                profile.lihat_saldo()

            elif pilih == "3":
                profile.isi_saldo()

            elif pilih == "4":
                profile.lihat_wishlist()

                tambah = input("\nMau tambah wishlist? (y/n) : ").lower()

                if tambah == "y":
                    profile.tambah_wishlist()
                else:
                    print("Baiklah...")

            elif pilih == "5":
                profile.lihat_riwayat_booking()

                undo = input("\nMau undo booking terakhir? (y/n) : ").lower()

                if undo == "y":
                    profile.undo_booking_terakhir()
                else:
                    print("Baiklah...")

            elif pilih == "0":
                break

            else:
                print("Pilihan tidak tersedia.")

        except Exception as e:
            print("Terjadi kesalahan :", e)


def travel_menu(user):
    travel = TravelService(user)

    while True:
        try:
            print("\n" + "=" * 40)
            print("✈️ TRAVEL CENTER".center(40))
            print("=" * 40)
            travel.tampil_rekomendasi()
            print("1. Rekomendasi Destinasi")
            print("2. Lihat Penerbangan")
            print("3. Booking Penerbangan")
            print("0. Kembali")
            print("-" * 40)

            pilih = input("Pilih : ")

            if pilih == "1":
                print("Mau ditampilkan seluruhnya atau per kategori?")
                print("1. Tampilkan seluruhnya")
                print("2. Tampilkan per kategori")

                pilihan = input("Pilihan kamu : ")

                if pilihan == "1":
                    travel.rekomendasi_destinasi()

                elif pilihan == "2":
                    travel.destinasi_populer()

                else:
                    print("Pilihan tidak tersedia.")

            elif pilih == "2":
                print("Pilih metode melihat penerbangan")
                print("1. Lihat seluruh penerbangan")
                print("2. Lihat rute ke kota tertentu")
                print("3. Lihat penerbangan sesuai budget")

                pilihan = input("Pilihan : ")

                if pilihan == "1":
                    travel.lihat_seluruh_penerbangan()

                elif pilihan == "2":
                    travel.lihat_rute_penerbangan_langsung()

                elif pilihan == "3":
                    travel.cari_range_harga()

                else:
                    print("Pilihan tidak tersedia.")

            elif pilih == "3":
                travel.booking()

                lihat_riwayat = input(
                    "Mau lihat data pemesanan? (y/n) : "
                ).lower()

                if lihat_riwayat == "y":
                    travel.lihat_riwayat_booking()

            elif pilih == "0":
                break

            else:
                print("Pilihan tidak tersedia.")

        except Exception as e:
            print("Terjadi kesalahan :", e)


def main():
    auth = AuthService()

    while True:
        try:
            print("\n" + "=" * 40)
            print("✈️ TRIPBOOKING SYSTEM".center(40))
            print("=" * 40)
            print("1. Register")
            print("2. Login")
            print("0. Keluar")
            print("-" * 40)
 
            pilih = input("Pilih : ")

            if pilih == "1":
                auth.register()

            elif pilih == "2":
                user = auth.login()

                if user:
                    while True:
                        print("\n" + "=" * 40)
                        print("🏠 DASHBOARD".center(40))
                        print("=" * 40)
                        print("1. Profile Center")
                        print("2. Travel Center")
                        print("0. Logout")

                        menu = input("Pilih : ")

                        if menu == "1":
                            profile_menu(user)

                        elif menu == "2":
                            travel_menu(user)

                        elif menu == "0":
                            break

                        else:
                            print("Pilihan tidak tersedia.")

            elif pilih == "0":
                print("Terima kasih.")
                break

            else:
                print("Pilihan tidak tersedia.")

        except KeyboardInterrupt:
            print("\nProgram dihentikan.")
            break

        except Exception as e:
            print("Terjadi kesalahan :", e)


main()

