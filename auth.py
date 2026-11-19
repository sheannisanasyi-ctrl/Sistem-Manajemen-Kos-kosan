import time
import pwinput
from data import dataPengguna, sesi
from utils import bersihkanLayar, tekanEnter, tampilHeader


def login():
    for percobaan in range(1, 4):
        bersihkanLayar()
        tampilHeader("HALAMAN LOGIN")

        username = input("Username : ").strip().lower()
        password = pwinput.pwinput("Password : ")

        if username == "" and password == "":
            print("\n(!_!) Username dan Password tidak boleh kosong!")
            tekanEnter()
            continue

        if username == "":
            print("\n(!_!) Username tidak boleh kosong!")
            tekanEnter()
            continue

        if password == "":
            print("\n(!_!) Password tidak boleh kosong!")
            tekanEnter()
            continue

        if username not in dataPengguna:
            print(f"\n(>_<) Username '{username}' tidak terdaftar!")
            print(f"Sisa kesempatan: {3 - percobaan}")
            tekanEnter()
            continue

        if dataPengguna[username]["password"] != password:
            print("\n(>_<) OH, NO! Password yang kamu masukkan salah.")
            print(f"Sisa kesempatan: {3 - percobaan}")
            tekanEnter()
            continue

        sesi["penggunaLogin"] = username
        print()
        print(f"(^_^) YEAY! Selamat datang, {username.upper()}")
        tekanEnter()
        return True

    bersihkanLayar()
    print(" (!_!) AKUNMU DIKUNCI SEMENTARA!")
    print("\n Terlalu sering salah, nih!")
    print(" Tunggu sebentar, ya...")
    time.sleep(5)
    return False


def register():
    bersihkanLayar()
    tampilHeader("HALAMAN REGISTRASI")

    username = input("Username : ").strip().lower()

    if username == "":
        print("\n(!_!) Username tidak boleh kosong!")
        tekanEnter()
        return

    if username in dataPengguna:
        print(f"\n(>_<) Yah... Username '{username}' sudah terdaftar!")
        tekanEnter()
        return

    password = pwinput.pwinput("Password : ")

    if password == "":
        print("\n(!_!) Password tidak boleh kosong!")
        tekanEnter()
        return

    dataPengguna[username] = {
        "password": password,
        "level": "user",
        "saldo": 0,
        "kamarSewa": None,
    }

    print()
    print("(^_^) YEAY! Registrasi Berhasil!")
    print("Silakan login kembali.".center(50))
    tekanEnter()