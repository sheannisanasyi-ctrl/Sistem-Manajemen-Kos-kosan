import time
import pwinput
from data import dataPengguna, sesi
from utils import bersihkanLayar, tekanEnter


def login():
    for percobaan in range(1, 4):
        bersihkanLayar()
        print("=== LOGIN ===")
        username = input("Username : ").strip().lower()
        password = pwinput.pwinput("Password : ")

        if username in dataPengguna and dataPengguna[username]["password"] == password:
            sesi["penggunaLogin"] = username
            print(f"\nLogin berhasil. Selamat datang, {username}!")
            tekanEnter()
            return True

        print(f"\nUsername atau password salah. Sisa percobaan: {3 - percobaan}")
        tekanEnter()

    print("\nTerlalu banyak percobaan salah. Akun dikunci sementara.")
    time.sleep(3)
    return False


def register():
    bersihkanLayar()
    print("=== REGISTER ===")
    username = input("Username baru : ").strip().lower()

    if username == "":
        print("\nUsername tidak boleh kosong.")
        tekanEnter()
        return

    if username in dataPengguna:
        print("\nUsername sudah digunakan.")
        tekanEnter()
        return

    password = pwinput.pwinput("Password baru : ")
    if password == "":
        print("\nPassword tidak boleh kosong.")
        tekanEnter()
        return

    dataPengguna[username] = {
        "password": password,
        "level": "user",
        "saldo": 0,
        "kamarSewa": None,
    }
    print("\nRegistrasi berhasil. Silakan login.")
    tekanEnter()