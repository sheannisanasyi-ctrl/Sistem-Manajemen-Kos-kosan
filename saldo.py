from data import dataPengguna, sesi
from utils import formatRupiah


def topupSaldo():
    username = sesi["penggunaLogin"]
    saldo = dataPengguna[username]["saldo"]

    print('''
    ====== TOP UP SALDO ======
    ''')
    print(f"saldo anda tersisa: {formatRupiah(saldo)}")

    try:
        nominal = int(input("Nominal top up: "))
        
        if nominal <= 0:
            raise ValueError("Nominal harus lebih dari 0")
    except ValueError as pesan:
        print("Nominal harus angka lebih dari 0")
    else:
        dataPengguna[username]["saldo"] += nominal
        saldoSekarang = dataPengguna[username]["saldo"]
        print(f"saldo anda setelah top up: {formatRupiah(saldoSekarang)}")
 

def cekSaldo():
    username = sesi["penggunaLogin"]
    saldo = dataPengguna[username]["saldo"]

    print('''
    ======== SALDO ========
    ''')
    print(f"saldo anda tersisa: {formatRupiah(saldo)}")