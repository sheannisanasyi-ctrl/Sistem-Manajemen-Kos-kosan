# pemesanan.py - pesan kamar, riwayat, berhenti sewa (Orang 3)

from datetime import datetime
from prettytable import PrettyTable
from data import dataPengguna, daftarKamar, riwayatPemesanan, sesi
from utils import validasiAngka, formatRupiah
from kamar import lihatKamar


def pesanKamar():
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