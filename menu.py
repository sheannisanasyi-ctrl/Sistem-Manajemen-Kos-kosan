from data import dataPengguna, sesi, simpanData
from utils import (LEBAR, tekanEnter, formatRupiah, pilihMenu, siapkanLayar)
from kamar import kelolaKamar, lihatKamar
from dashboard import tampilDashboard
from grafik import tampilGrafik
from saldo import topupSaldo
from pemesanan import pesanKamar, lihatRiwayat, berhentiSewa


def tampilMenuAwal():
    siapkanLayar("SISTEM MANAJEMEN KOS")
    return pilihMenu("Pilih menu", ["Login", "Register", "Keluar"])


def menuAdmin():
    while True:
        siapkanLayar(f"MENU ADMIN - {sesi['penggunaLogin'].upper()}")
        pilihan = pilihMenu(
            "Pilih menu admin",
            ["Kelola Kamar", "Dashboard", "Grafik Pendapatan", "Logout"],
        )

        if pilihan == "Kelola Kamar":
            kelolaKamar()
        elif pilihan == "Dashboard":
            siapkanLayar("HALAMAN DASHBOARD")
            tampilDashboard()
            tekanEnter()
        elif pilihan == "Grafik Pendapatan":
            siapkanLayar("GRAFIK PENDAPATAN KOS")
            tampilGrafik()
            tekanEnter()
        else:
            sesi["penggunaLogin"] = None
            break


def menuUser():
    while True:
        username = sesi["penggunaLogin"]
        saldo = dataPengguna[username]["saldo"]
        siapkanLayar(f"MENU USER - {username.upper()}")
        print(f"Saldo: {formatRupiah(saldo)}".center(LEBAR))
        print()
        pilihan = pilihMenu(
            "Pilih menu user",
            ["Lihat Kamar Kosong", "Pesan Kamar", "Top Up Saldo",
             "Riwayat Pemesanan", "Berhenti Sewa", "Logout"],
        )

        if pilihan == "Lihat Kamar Kosong":
            siapkanLayar("KAMAR KOSONG")
            lihatKamar(hanyaKosong=True)
            tekanEnter()
        elif pilihan == "Pesan Kamar":
            siapkanLayar("FORM PEMESANAN KAMAR")
            if pesanKamar():
                simpanData()
            tekanEnter()
        elif pilihan == "Top Up Saldo":
            siapkanLayar("TOP UP SALDO")
            if topupSaldo():
                simpanData()
            tekanEnter()
        elif pilihan == "Riwayat Pemesanan":
            siapkanLayar("RIWAYAT PEMESANAN SAYA")
            lihatRiwayat()
            tekanEnter()
        elif pilihan == "Berhenti Sewa":
            siapkanLayar("FORM BERHENTI SEWA")
            if berhentiSewa():
                simpanData()
            tekanEnter()
        else:
            sesi["penggunaLogin"] = None
            break