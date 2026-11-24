from datetime import datetime

from data import dataPengguna, daftarKamar, riwayatPemesanan, sesi
from utils import (formatRupiah, pilihMenu, buatTabel,
                   pesanSukses, pesanPeringatan, pesanGagal)
from kamar import lihatKamar, inputIdKamar


def adaKamarKosong():
    for kamar in daftarKamar.values():
        if kamar["status"] == "Kosong":
            return True
    return False


def pesanKamar():
    username = sesi["penggunaLogin"]
    akun = dataPengguna[username]

    if akun["kamarSewa"] is not None:
        pesanGagal("Eits, kamu masih punya kamar sewaan nih!")
        return False
    if not adaKamarKosong():
        pesanGagal("Yah, lagi nggak ada kamar kosong nih. Cek lagi nanti ya!")
        return False

    lihatKamar(hanyaKosong=True)
    idKamar = inputIdKamar()
    if idKamar is None:
        return False

    kamar = daftarKamar[idKamar]
    if kamar["status"] != "Kosong":
        pesanGagal(f"Yah, kamar {idKamar} sudah ada penyewanya!")
        return False

    harga = kamar["harga"]
    if akun["saldo"] < harga:
        kurang = harga - akun["saldo"]
        pesanGagal(f"Saldomu kurang {formatRupiah(kurang)} nih, top up dulu yuk!")
        return False

    akun["saldo"] -= harga
    kamar["status"] = "Terisi"
    kamar["penyewa"] = username
    akun["kamarSewa"] = idKamar
    riwayatPemesanan.append({
        "username": username,
        "idKamar": idKamar,
        "harga": harga,
        "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })
    pesanSukses(f"YEAY! Kamar {idKamar} sekarang punyamu, harganya {formatRupiah(harga)}!")
    return True


def lihatRiwayat():
    username = sesi["penggunaLogin"]
    riwayatUser = [item for item in riwayatPemesanan if item["username"] == username]
    if not riwayatUser:
        pesanPeringatan("Kamu belum pernah pesan kamar nih!")
        return

    tabel = buatTabel("RIWAYAT PEMESANAN", ["ID Kamar", "Harga", "Tanggal Pemesanan"])
    for item in riwayatUser:
        tabel.add_row([item["idKamar"], formatRupiah(item["harga"]), item["tanggal"]])
    print(tabel)


def berhentiSewa():
    username = sesi["penggunaLogin"]
    idKamar = dataPengguna[username]["kamarSewa"]
    if idKamar is None:
        pesanGagal("Kamu kan belum nyewa kamar!")
        return False

    konfirmasi = pilihMenu(
        f"Yakin mau berhenti sewa kamar {idKamar}? (uang sewa tidak dikembalikan)",
        ["Ya, berhenti sewa", "Tidak jadi"],
    )
    if konfirmasi == "Ya, berhenti sewa":
        daftarKamar[idKamar]["status"] = "Kosong"
        daftarKamar[idKamar]["penyewa"] = None
        dataPengguna[username]["kamarSewa"] = None
        pesanSukses("YEAY! Kamu sudah berhenti sewa kamar!")
        return True
    pesanPeringatan("Oke, batal berhenti sewa!")
    return False