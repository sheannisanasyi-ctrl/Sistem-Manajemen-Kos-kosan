from datetime import datetime
from prettytable import PrettyTable
from data import dataPengguna, daftarKamar, riwayatPemesanan, sesi
from utils import formatRupiah
from kamar import lihatKamar


def pesanKamar():
    username = sesi["penggunaLogin"]

    if dataPengguna[username]["kamarSewa"] is not None:
        print("Anda sudah menyewa kamar.")
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
            print("Saldo tidak cukup.")
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
        print("Belum ada riwayat pemesanan.")
        return

    tabel = PrettyTable(["ID Kamar", "Harga", "Tanggal Pemesanan"])
    for i in riwayat:
        tabel.add_row([i["idKamar"], formatRupiah(i["harga"]), i["tanggal"]])
    print(tabel)


def berhentiSewa():
    username = sesi["penggunaLogin"]
    idKamar = dataPengguna[username]["kamarSewa"]

    if idKamar is None:
        print("Anda belum menyewa kamar.")
        return

    konfirmasi = input(f"Yakin berhenti menyewa kamar {idKamar}? (y/n): ").strip().lower()
    if konfirmasi == "y":
        daftarKamar[idKamar]["status"] = "Kosong"
        daftarKamar[idKamar]["penyewa"] = None
        dataPengguna[username]["kamarSewa"] = None
        print("Berhasil berhenti sewa. Saldo tidak dikembalikan.")
    else:
        print("Dibatalkan.")


def berhentiSewa():
    # TODO: sesuai flowchart berhentiSewa()
    # - jika kamarSewa user None: "Anda belum menyewa kamar"
    # - konfirmasi y/n
    # - daftarKamar[idKamar]: status "Kosong", penyewa None
    # - dataPengguna[username]["kamarSewa"] = None
    # - saldo tidak dikembalikan
    pass