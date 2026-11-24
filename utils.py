import os

import inquirer
from prettytable import PrettyTable, ALL

LEBAR = 50


def bersihkanLayar():
    os.system("cls" if os.name == "nt" else "clear")


def tekanEnter():
    input("\nTekan Enter untuk lanjut...")


def validasiAngka(teks):
    return teks.isascii() and teks.isdigit()


def formatRupiah(angka):
    return f"Rp{angka:,.0f}".replace(",", ".")


def buatTabel(judul, kolom):
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = kolom
    tabel.align = "c"
    tabel.hrules = ALL
    return tabel


def pilihMenu(judul, daftarPilihan):
    pertanyaan = [
        inquirer.List("pilihan", message=judul, choices=daftarPilihan)
    ]
    jawaban = inquirer.prompt(pertanyaan)
    if jawaban is None:
        return None
    return jawaban["pilihan"]


def tampilHeader(subjudul, lebar=LEBAR):
    print("=" * lebar)
    print("KOSKU".center(lebar))
    print(subjudul.center(lebar))
    print("=" * lebar)


def siapkanLayar(subjudul):
    bersihkanLayar()
    tampilHeader(subjudul)


def pesanSukses(teks):
    print(f"\n(^_^) {teks}")


def pesanPeringatan(teks):
    print(f"\n(!_!) {teks}")


def pesanGagal(teks):
    print(f"\n(>_<) {teks}")