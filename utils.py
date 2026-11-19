import os
import inquirer
from data import daftarKamar


def bersihkanLayar():
    os.system("cls" if os.name == "nt" else "clear")


def tekanEnter():
    input("\nTekan Enter untuk melanjutkan...")


def validasiAngka(teks):
    if teks.isdigit():
        return int(teks) > 0
    return False


def formatRupiah(angka):
    return f"Rp{angka:,.0f}".replace(",", ".")


def generateIdBaru(angka=1):
    idBaru = f"K{angka:03d}"
    if idBaru not in daftarKamar:
        return idBaru
    return generateIdBaru(angka + 1)


def pilihMenu(judul, daftarPilihan):
    pertanyaan = [
        inquirer.List("pilihan", message=judul, choices=daftarPilihan)
    ]
    jawaban = inquirer.prompt(pertanyaan)
    if jawaban is None:
        return None
    return jawaban["pilihan"]

def tampilHeader(subjudul, lebar=50):
    print("=" * lebar)
    print("KOSKU".center(lebar))
    print(subjudul.center(lebar))
    print("=" * lebar)