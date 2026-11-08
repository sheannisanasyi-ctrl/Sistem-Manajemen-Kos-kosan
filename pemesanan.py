# pemesanan.py - pesan kamar dan riwayat (Orang 3)

from datetime import datetime
from data import dataPengguna, daftarKamar, riwayatPemesanan, sesi
from kamar import lihatKamar


def pesanKamar():
    # TODO: (user)
    # - cek user belum punya kamar (kamarSewa harus None)
    # - lihatKamar(hanyaKosong=True), input ID kamar
    # - ID harus ada dan status "Kosong"
    # - saldo >= harga, jika tidak tampilkan "Saldo tidak cukup"
    # - saldo dikurangi harga, status kamar "Terisi", isi penyewa dan kamarSewa
    # - catat ke riwayatPemesanan (idKamar, harga, tanggal dari datetime.now())
    pass


def lihatPemesanan():
    # TODO: (admin) tampilkan semua riwayat semua user dalam tabel
    pass


def lihatRiwayat():
    # TODO: (user) tampilkan riwayat milik sesi["penggunaLogin"] saja
    pass