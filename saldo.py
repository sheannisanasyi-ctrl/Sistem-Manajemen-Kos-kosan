# saldo.py - top up dan cek saldo, keduanya untuk USER yang sedang login (Orang 3)

from data import dataPengguna, sesi
from utils import formatRupiah


def topupSaldo():
    username = sesi["penggunaLogin"]
    target = dataPengguna.get(username)
    saldo = target.get("saldo")

    print('''
    ====== TOP UP SALDO ======
    ''')
    print(f"saldo anda tersisa: {formatRupiah(saldo)}")

    try:
        nominal = int(input("Nominal top up: "))
        
        if nominal <= 0:
            raise ValueError("Nominal harus lebih dari 0")
    except ValueError as pesan:
        pesan("Nominal harus angka lebih dari 0")
    else:
        dict[username]["saldo"] += nominal
        print(f"saldo anda setelah top up: {formatRupiah(saldo)}")
    # TODO: sesuai flowchart topupSaldo(), memakai try-except-else dan raise (modul 7.2)
    # - username = sesi["penggunaLogin"], tampilkan saldo saat ini (formatRupiah)
    # - try:
    #       nominal = int(input("Nominal top up : "))
    #       jika nominal <= 0: raise ValueError("Nominal harus lebih dari 0")
    #   except ValueError as pesan:
    #       tampilkan pesan error ("Nominal harus angka lebih dari 0")
    #   else:
    #       saldo bertambah sebesar nominal, tampilkan saldo baru
    pass


def cekSaldo():
    username = sesi["penggunaLogin"]
    target = dataPengguna.get(username)
    saldo = target.get("saldo")

    print('''
    ======== SALDO ========
    ''')
    print(f"saldo anda tersisa: {formatRupiah(saldo)}")
    # TODO: tampilkan saldo milik sesi["penggunaLogin"] (formatRupiah)
    pass