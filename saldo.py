from data import dataPengguna, sesi, maksTopup
from utils import formatRupiah, validasiAngka, pesanSukses, pesanPeringatan


def topupSaldo():
    username = sesi["penggunaLogin"]
    print(f"Saldo saat ini: {formatRupiah(dataPengguna[username]['saldo'])}")
    nominal = input("Nominal top up: ").strip()
    if nominal == "":
        pesanPeringatan("Nominal top up jangan dikosongin dong!")
        return False
    if not validasiAngka(nominal):
        pesanPeringatan("Nominal top up harus angka bulat lebih dari 0 ya, contoh: 500000")
        return False

    nominal = int(nominal)
    if nominal <= 0:
        pesanPeringatan("Nominal top up harus lebih dari 0 ya!")
        return False
    if nominal > maksTopup:
        pesanPeringatan(f"Sekali top up maksimal {formatRupiah(maksTopup)} ya!")
        return False

    dataPengguna[username]["saldo"] += nominal
    saldoSekarang = dataPengguna[username]["saldo"]
    pesanSukses(f"YEAY! Top up berhasil, saldomu sekarang {formatRupiah(saldoSekarang)}!")
    return True