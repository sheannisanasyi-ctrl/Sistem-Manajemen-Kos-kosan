from datetime import datetime
from prettytable import PrettyTable
from data import dataPengguna, daftarKamar, riwayatPemesanan, sesi
from utils import formatRupiah
from kamar import lihatKamar


def pesanKamar():
    username = sesi["penggunaLogin"]

    if dataPengguna[username]["kamarSewa"] is not None:
        print("Kamu sudah menyewa kamar!")
        return

    lihatKamar(hanyaKosong=True)
    idKamar = input("Masukkan ID Kamar: ").strip().upper()

    if idKamar not in daftarKamar:
        print("ID kamar tidak diketahui.")
    elif daftarKamar[idKamar]["status"] != "Kosong":
        print(f"Kamar {idKamar} sudah ada penyewa.")
    else:
        harga = daftarKamar[idKamar]["harga"]
        if dataPengguna[username]["saldo"] < harga:
            print("Saldomu tidak cukup untuk menyewa kamar ini.")
        else:
            dataPengguna[username]["saldo"] -= harga
            daftarKamar[idKamar]["status"] = "Terisi"
            daftarKamar[idKamar]["penyewa"] = username
            dataPengguna[username]["kamarSewa"] = idKamar
            riwayatPemesanan.append({
                "username": username,
                "idKamar": idKamar,
                "harga": harga,
                "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            })
            print(f"Berhasil menyewa kamar {idKamar} dengan harga {formatRupiah(harga)}.")


def lihatRiwayat():
    username = sesi["penggunaLogin"]
    riwayat = [i for i in riwayatPemesanan if i["username"] == username]

    if not riwayat:
        print("Kamu belum pernah melakukan pemesanan.")
        return

    tabel = PrettyTable(["ID Kamar", "Harga", "Tanggal Pemesanan"])
    for i in riwayat:
        tabel.add_row([i["idKamar"], formatRupiah(i["harga"]), i["tanggal"]])
    print(tabel)


def berhentiSewa():
    username = sesi["penggunaLogin"]
    idKamar = dataPengguna[username]["kamarSewa"]

    if idKamar is None:
        print("Kamu belum menyewa kamar!")
        return

    konfirmasi = input(f"Yakin berhenti menyewa kamar {idKamar}? (y/n): ").strip().lower()
    if konfirmasi == "y":
        daftarKamar[idKamar]["status"] = "Kosong"
        daftarKamar[idKamar]["penyewa"] = None
        dataPengguna[username]["kamarSewa"] = None
        print("Berhasil berhenti menyewa kamar.")
    else:
        print("Dibatalkan.")