from data import dataPengguna, sesi
from utils import bersihkanLayar, tekanEnter, formatRupiah, pilihMenu
from kamar import kelolaKamar, lihatKamar
from dashboard import tampilDashboard
from grafik import tampilGrafik
from saldo import topupSaldo, cekSaldo
from pemesanan import pesanKamar, lihatRiwayat, berhentiSewa


def tampilMenuAwal():
    bersihkanLayar()
    print("=" * 44)
    print("KOSKU".center(44))
    print("Sistem Manajemen Kos".center(44))
    print("=" * 44)
    return pilihMenu("Pilih menu", ["Login", "Register", "Keluar"])


def menuAdmin():
    while True:
        bersihkanLayar()
        print("=" * 55)
        print("KOSKU".center(55))
        print(f"MENU ADMIN - {sesi['penggunaLogin'].upper()}".center(55))
        print("=" * 55)
        
        pilihan = pilihMenu(
            "Pilih menu admin",
            ["Kelola Kamar", "Dashboard", "Grafik Pendapatan", "Logout"],
        )

        if pilihan == "Kelola Kamar":
            kelolaKamar()  
        elif pilihan == "Dashboard":
            bersihkanLayar()
            print("=" * 44)
            print("KOSKU".center(44))
            print("HALAMAN DASHBOARD".center(44))
            print("=" * 44)
            tampilDashboard()
            tekanEnter()
        elif pilihan == "Grafik Pendapatan":
            bersihkanLayar()
            print("=" * 44)
            print("KOSKU".center(44))
            print("GRAFIK PENDAPATAN KOS".center(44))
            print("=" * 44)
            tampilGrafik()
        else:
            sesi["penggunaLogin"] = None
            break


def menuUser():
    while True:
        username = sesi["penggunaLogin"]
        saldo = dataPengguna[username]["saldo"]
        
        bersihkanLayar()
        print("=" * 44)
        print("KOSKU".center(44))
        print(f"MENU USER - {username.upper()}".center(44))
        print(f"Saldo: {formatRupiah(saldo)}".center(44))
        print("=" * 44)
        
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
            print("=" * 44)
            print("KOSKU".center(44))
            print("DAFTAR KAMAR KOSONG".center(44))
            print("=" * 44)
            lihatKamar(hanyaKosong=True)
            tekanEnter()
        elif pilihan == "Pesan Kamar":
            bersihkanLayar()
            print("=" * 44)
            print("KOSKU".center(44))
            print("FORM PEMESANAN KAMAR".center(44))
            print("=" * 44)
            pesanKamar()
            tekanEnter()
        elif pilihan == "Top Up Saldo":
            bersihkanLayar()
            topupSaldo()
            tekanEnter()
        elif pilihan == "Riwayat Pemesanan":
            bersihkanLayar()
            print("=" * 44)
            print("KOSKU".center(47))
            print("RIWAYAT PEMESANAN SAYA".center(47))
            print("=" * 47)
            lihatRiwayat()
            tekanEnter()
        elif pilihan == "Berhenti Sewa":
            bersihkanLayar()
            print("=" * 44)
            print("KOSKU".center(44))
            print("FORM BERHENTI SEWA".center(44))
            print("=" * 44)
            berhentiSewa()
            tekanEnter()
        else:
            sesi["penggunaLogin"] = None
            break