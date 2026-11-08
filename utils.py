import os
from data import daftarKamar


def bersihkanLayar():
    os.system("cls" if os.name == "nt" else "clear")


def tekanEnter():
    input("\Tekan Enter untuk melanjutkan...")


def validasiAngka(teks):
    if teks.isdigit():
        return int(teks) > 0
    return False


def formatRupiah(angka):
    return f"Rp{angka:,.0f}".replace(",", ".")


def generateIdBaru():
    angka = 1
    while True:
        idBaru = f"K{angka:03d}"
        if idBaru not in daftarKamar:
            return idBaru
        angka += 1