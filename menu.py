from data import dataPengguna, sesi
from utils import bersihkanLayar, tekanEnter, formatRupiah, pilihMenu
from kamar import kelolaKamar, lihatKamar
from dashboard import tampilDashboard
from saldo import topupSaldo, cekSaldo
from pemesanan import pesanKamar, lihatRiwayat, berhentiSewa


def tampilMenuAwal():
    bersihkanLayar()
    print("=" * 40)
    print("      KOSKU - SISTEM MANAJEMEN KOS")
    print("=" * 40)
    return pilihMenu("Pilih menu", ["Login", "Register", "Keluar"])


def menuAdmin():
    while True:
        bersihkanLayar()
        print("=" * 40)
        print(f"  MENU ADMIN - {sesi['penggunaLogin']}")
        print("=" * 40)
        pilihan = pilihMenu(
            "Pilih menu",
            ["Kelola Kamar", "Dashboard", "Grafik Okupansi", "Logout"],
        )

        if pilihan == "Kelola Kamar":
            kelolaKamar()  
        elif pilihan == "Dashboard":
            bersihkanLayar()
            tampilDashboard()
            tekanEnter()
        elif pilihan == "Grafik Okupansi":
            tampilGrafik()
        else:
            sesi["penggunaLogin"] = None
            break


def menuUser():
    while True:
        username = sesi["penggunaLogin"]
        saldo = dataPengguna[username]["saldo"]
        bersihkanLayar()
        print("=" * 40)
        print(f"  MENU USER - {username}")
        print(f"  Saldo: {formatRupiah(saldo)}")
        print("=" * 40)
        pilihan = pilihMenu(
            "Pilih menu",
            [
                "Lihat Kamar Kosong",
                "Pesan Kamar",
                "Top Up Saldo",
                "Cek Saldo",
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
            pesanKamar()
            tekanEnter()
        elif pilihan == "Top Up Saldo":
            bersihkanLayar()
            topupSaldo()
            tekanEnter()
        elif pilihan == "Cek Saldo":
            bersihkanLayar()
            cekSaldo()
            tekanEnter()
        elif pilihan == "Riwayat Pemesanan":
            bersihkanLayar()
            lihatRiwayat()
            tekanEnter()
        elif pilihan == "Berhenti Sewa":
            bersihkanLayar()
            berhentiSewa()
            tekanEnter()
        else:
            sesi["penggunaLogin"] = None
            break