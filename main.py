from data import dataPengguna, sesi, muatData, simpanData
from utils import bersihkanLayar, tekanEnter
from auth import login, register
from menu import tampilMenuAwal, menuAdmin, menuUser


def main():
    muatData()
    try:
        while True:
            pilihan = tampilMenuAwal()

            if pilihan == "Login":
                if login():
                    level = dataPengguna[sesi["penggunaLogin"]]["level"]
                    if level == "admin":
                        menuAdmin()
                    else:
                        menuUser()
            elif pilihan == "Register":
                register()
            elif pilihan == "Keluar" or pilihan is None:
                bersihkanLayar()
                print("Terima kasih telah menggunakan KosKu.")
                break
            else:
                print("Pilihan tidak valid.")
                tekanEnter()
    except KeyboardInterrupt:
        print("\nProgram dihentikan.")
    finally:
        simpanData()


if __name__ == "__main__":
    main()