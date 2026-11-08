# main.py - titik masuk program (Orang 1)

from data import dataPengguna, sesi, muatData, simpanData
from auth import login, register
from menu import tampilMenuAwal, menuAdmin, menuUser


def main():
    # TODO: muatData(), lalu while True:
    # - tampilMenuAwal(), input pilihan
    # - 1: login(); jika berhasil cek level -> menuAdmin() atau menuUser()
    # - 2: register()
    # - 3: pesan terima kasih, simpanData(), break
    # - selain itu: "Pilihan tidak valid"
    pass


# Dua baris ini wajib pakai underscore ganda, itu aturan bawaan Python
if __name__ == "__main__":
    main()