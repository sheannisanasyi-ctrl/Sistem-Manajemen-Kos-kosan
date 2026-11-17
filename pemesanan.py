from datetime import datetime
from prettytable import PrettyTable
from data import dataPengguna, daftarKamar, riwayatPemesanan, sesi
from utils import validasiAngka, formatRupiah
from kamar import lihatKamar


def pesanKamar():
    username = sesi["penggunaLogin"]
    kamarSewa = dataPengguna[username]["kamarSewa"]
    saldo = dataPengguna[username]["saldo"]

    if kamarSewa is None:
        lihatKamar(hanyaKosong=True)

        try:
            inpIDkamar = input("Masukkan ID Kamar: ").strip().capitalize()


            if inpIDkamar in daftarKamar:
                penyewa = daftarKamar[inpIDkamar]["penyewa"]

                if penyewa is None:
                    harga = daftarKamar[inpIDkamar]["harga"]

                    if saldo >= harga:
                        saldo -= harga
                        harga = daftarKamar[inpIDkamar]["harga"]
                        penyewa = username
                        daftarKamar[inpIDkamar]["status"] = "Terisi"
                        kamarSewa = inpIDkamar
                        riwayatPemesanan[username, inpIDkamar, harga, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                        print(f"Berhasil menyewa kamar {inpIDkamar} dengan harga {harga}")
                    else:
                        print("saldo anda tidak cukup")
                else:
                    print(f"ID Kamar {inpIDkamar} sudah ada penyewa")
            else:
                print("ID kamar tidak diketahui")
        except ValueError:
            print("ID kamar atau masukkan tidak di ketahui")
    else:
        print("Anda sudah menyewa kamar")
    # TODO: sesuai flowchart pesanKamar()
    # - user sudah punya kamar (kamarSewa tidak None): tolak
    # - lihatKamar(hanyaKosong=True), input ID kamar
    # - ID harus ada dan status "Kosong"
    # - saldo >= harga, jika tidak: "Saldo tidak cukup"
    # - saldo dikurangi harga
    # - daftarKamar: status "Terisi", penyewa = username
    # - dataPengguna: kamarSewa = ID kamar
    # - catat ke riwayatPemesanan: username, idKamar, harga, tanggal (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    pass


def lihatRiwayat():
    username = sesi["penggunaLogin"]
    riwayat = [i for i in riwayatPemesanan if i.get("username") == username]

    if riwayat:
        tabel = PrettyTable(["username", "ID Kamar", "Harga", "Tanggal Pemesanan"])
        tabel.align = "c"

        for i in riwayat:
            tabel.add_row([
                i["username"],
                i["idKamar"],
                i[formatRupiah("harga")],
                i["tanggal"]
            ])

        print(tabel)
    else:
        print("Belum ada riwayat pemesanan")
    # TODO: tampilkan riwayat milik sesi["penggunaLogin"] saja (tabel PrettyTable)
    # - jika tidak ada: "Belum ada riwayat pemesanan"
    pass


def berhentiSewa():
    # TODO: sesuai flowchart berhentiSewa()
    # - jika kamarSewa user None: "Anda belum menyewa kamar"
    # - konfirmasi y/n
    # - daftarKamar[idKamar]: status "Kosong", penyewa None
    # - dataPengguna[username]["kamarSewa"] = None
    # - saldo tidak dikembalikan
    pass