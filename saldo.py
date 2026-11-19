from data import dataPengguna, sesi
from utils import formatRupiah, tampilHeader


def topupSaldo():
    username = sesi["penggunaLogin"]
    saldo = dataPengguna[username]["saldo"]

    tampilHeader("Top Up Saldo")
    print(f"Saldo Anda tersisa: {formatRupiah(saldo)}")

    try:
        nominal = input("Nominal top up: ").strip()
        if nominal == "":
            raise ValueError("kosong")
        nominal = int(nominal)
        if nominal <= 0:
            raise ValueError("kurangDariNol")
    except ValueError as err:
        kodeError = str(err)
        if kodeError == "kosong":
            print("[-] Nominal top up tidak boleh kosong!")
        elif kodeError == "kurangDariNol":
            print("[-] Nominal top up harus lebih dari 0!")
        else:
            print("[-] Nominal top up harus berupa angka!")
    else:
        dataPengguna[username]["saldo"] += nominal
        saldoSekarang = dataPengguna[username]["saldo"]
        print()
        print(f"[+] Top up berhasil! Saldomu sekarang: {formatRupiah(saldoSekarang)}")