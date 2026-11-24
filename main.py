from data import dataPengguna, sesi, muatData, simpanData
from utils import (bersihkanLayar, tekanEnter, siapkanLayar,
                   pesanSukses, pesanPeringatan, pesanGagal)
from auth import login, register
from menu import tampilMenuAwal, menuAdmin, menuUser


def main():
    status = muatData()
    if status == "gagalBaca":
        pesanGagal("Waduh, file data nggak bisa dibaca! Cek izin file 'dataKosku.json' ya.")
        return

    try:
        if status == "rusak":
            pesanPeringatan("File data-nya rusak, jadi sudah dicadangkan (.rusak-...) "
                            "dan KosKu pakai data awal dulu ya!")
            tekanEnter()

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
                siapkanLayar("HALAMAN REGISTRASI")
                if register():
                    simpanData()
                tekanEnter()
            elif pilihan == "Keluar" or pilihan is None:
                bersihkanLayar()
                pesanSukses("Makasih udah pakai KosKu, sampai jumpa lagi!")
                break
            else:
                pesanPeringatan("Pilihannya nggak valid nih!")
                tekanEnter()
    except (KeyboardInterrupt, EOFError):
        print()
        pesanPeringatan("Program dihentikan, sampai jumpa!")
    finally:
        simpanData()


if __name__ == "__main__":
    main()