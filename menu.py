from data import dataPengguna, sesi
from utils import bersihkanLayar, tekanEnter, formatRupiah, pilihMenu, tampilHeader
from kamar import kelolaKamar, lihatKamar
from dashboard import tampilDashboard
from grafik import tampilGrafik
from saldo import topupSaldo
from pemesanan import pesanKamar, lihatRiwayat, berhentiSewa


def tampilMenuAwal():
    bersihkanLayar()
    tampilHeader("Sistem Manajemen Kos")
    return pilihMenu("Pilih menu", ["Login", "Register", "Keluar"])


def menuAdmin():
    while True:
        bersihkanLayar()
        tampilHeader(f"MENU ADMIN - {sesi['penggunaLogin'].upper()}")

        pilihan = pilihMenu(
            "Pilih menu admin",
            ["Kelola Kamar", "Dashboard", "Grafik Pendapatan", "Logout"],
        )

        if pilihan == "Kelola Kamar":
            kelolaKamar()
        elif pilihan == "Dashboard":
            bersihkanLayar()
            tampilHeader("HALAMAN DASHBOARD")
            tampilDashboard()
            tekanEnter()
        elif pilihan == "Grafik Pendapatan":
            bersihkanLayar()
            tampilHeader("GRAFIK PENDAPATAN KOS")
            tampilGrafik()
        else:
            sesi["penggunaLogin"] = None
            break


def menuUser():
    while True:
        username = sesi["penggunaLogin"]
        saldo = dataPengguna[username]["saldo"]

        bersihkanLayar()
        tampilHeader(f"MENU USER - {username.upper()}")
        print(f"Saldo: {formatRupiah(saldo)}".center(50))
        print()

        pilihan = pilihMenu(
            "Pilih menu user",
            [
                "Lihat Kamar Kosong",
                "Pesan Kamar",
                "Top Up Saldo",
                "Riwayat Pemesanan",
                "Berhenti Sewa",
                "Logout",
            ],
        )

        if pilihan == "Lihat Kamar Kosong":
            bersihkanLayar()
            lihatKamar(hanyaKosong=True)
            tekanEnter()
        elif pilihan == "Pesan Kamar":
            bersihkanLayar()
            tampilHeader("FORM PEMESANAN KAMAR")
            pesanKamar()
            tekanEnter()
        elif pilihan == "Top Up Saldo":
            bersihkanLayar()
            topupSaldo()
            tekanEnter()
        elif pilihan == "Riwayat Pemesanan":
            bersihkanLayar()
            tampilHeader("RIWAYAT PEMESANAN SAYA")
            lihatRiwayat()
            tekanEnter()
        elif pilihan == "Berhenti Sewa":
            bersihkanLayar()
            tampilHeader("FORM BERHENTI SEWA")
            berhentiSewa()
            tekanEnter()
        else:
            sesi["penggunaLogin"] = None
            break