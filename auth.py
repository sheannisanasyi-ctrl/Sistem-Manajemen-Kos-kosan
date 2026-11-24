import math
import sys
import time

import pwinput

from data import dataPengguna, sesi
from keamanan import hashPassword, verifikasiPassword
from utils import (bersihkanLayar, tekanEnter, siapkanLayar,
                   pesanSukses, pesanPeringatan, pesanGagal)

maksPercobaan = 3
durasiKunci = 10
minimalUsername = 4
maksUsername = 20
minimalPassword = 3


def sisaWaktuKunci():
    sisa = sesi["terkunciSampai"] - time.time()
    return max(0, math.ceil(sisa))


def bersihkanBufferInput():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        try:
            import termios
            termios.tcflush(sys.stdin, termios.TCIFLUSH)
        except Exception:
            pass


def countdownKunci():
    bersihkanLayar()
    pesanGagal("YAH, LOGIN DIKUNCI SEMENTARA!")
    pesanPeringatan("Kebanyakan salah nih, tunggu sebentar ya...")
    print()
    while True:
        sisa = sisaWaktuKunci()
        if sisa <= 0:
            break
        print(f"\r(!_!) Coba lagi dalam {sisa} detik...   ", end="", flush=True)
        time.sleep(1)
    print()
    bersihkanBufferInput()
    bersihkanLayar()
    pesanSukses("Kunci login sudah dibuka, yuk coba lagi!")
    tekanEnter()


def login():
    if sisaWaktuKunci() > 0:
        countdownKunci()
        return False

    percobaan = 0
    while percobaan < maksPercobaan:
        siapkanLayar("HALAMAN LOGIN")
        username = input("Username : ").strip().lower()
        password = pwinput.pwinput("Password : ")

        kosong = []
        if username == "":
            kosong.append("Username")
        if password == "":
            kosong.append("Password")
        if kosong:
            pesanPeringatan(" dan ".join(kosong) + " jangan dikosongin dong!")
            tekanEnter()
            continue

        akun = dataPengguna.get(username)
        tersimpan = akun["password"] if akun is not None else None
        if not verifikasiPassword(password, tersimpan):
            percobaan += 1
            pesanGagal("OH, NO! Username atau password salah!")
            sisa = maksPercobaan - percobaan
            if sisa > 0:
                pesanPeringatan(f"Sisa kesempatan: {sisa}")
            tekanEnter()
            continue

        sesi["penggunaLogin"] = username
        pesanSukses(f"YEAY! Selamat datang, {username.upper()}!")
        tekanEnter()
        return True

    sesi["terkunciSampai"] = time.time() + durasiKunci
    countdownKunci()
    return False


def register():
    username = input("Username : ").strip().lower()
    if username == "":
        pesanPeringatan("Username jangan dikosongin dong!")
        return False
    if not (username.isascii() and username.isalnum()):
        pesanPeringatan("Username cuma boleh huruf dan angka ya!")
        return False
    if not minimalUsername <= len(username) <= maksUsername:
        pesanPeringatan(f"Username harus {minimalUsername}-{maksUsername} karakter ya!")
        return False
    if username in dataPengguna:
        pesanGagal(f"Yah... username '{username}' sudah ada yang pakai!")
        return False

    password = pwinput.pwinput("Password : ")
    if password == "":
        pesanPeringatan("Password jangan dikosongin dong!")
        return False
    if len(password) < minimalPassword:
        pesanPeringatan(f"Password minimal {minimalPassword} karakter ya!")
        return False

    konfirmasi = pwinput.pwinput("Konfirmasi Password : ")
    if konfirmasi != password:
        pesanPeringatan("Konfirmasi password nggak cocok nih!")
        return False

    dataPengguna[username] = {
        "password": hashPassword(password),
        "level": "user",
        "saldo": 0,
        "kamarSewa": None,
    }
    pesanSukses("YEAY! Registrasi berhasil!")
    pesanSukses("Yuk login dulu buat mulai pakai KosKu!")
    return True