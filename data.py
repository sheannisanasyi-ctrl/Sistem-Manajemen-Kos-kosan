# data.py - penyimpanan data bersama (Orang 1)
# Semua file lain mengimpor data dari sini.
# Catatan: jangan tulis ulang variabelnya dengan "=" di file lain, cukup ubah isinya
# (contoh: dataPengguna["user1"]["saldo"] -= harga).

import json

namaFile = "dataKosku.json"

# Tipe kamar bersifat tetap, jadi pakai tuple (materi tuple)
tipeKamar = ("Standar", "AC", "VIP")

dataPengguna = {
    "admin": {"password": "admin123", "level": "admin", "saldo": 0, "kamarSewa": None},
    "user1": {"password": "user123", "level": "user", "saldo": 500000, "kamarSewa": None},
}

daftarKamar = {
    "K001": {"tipe": "AC", "harga": 900000, "fasilitas": "WiFi, KM dalam", "status": "Kosong", "penyewa": None},
}

# isi tiap riwayat: {"username", "idKamar", "harga", "tanggal"}
riwayatPemesanan = []

# Sesi login disimpan di dictionary supaya bisa diubah dari file lain
sesi = {"penggunaLogin": None}


def muatData():
    # TODO: baca namaFile (JSON) ke dataPengguna, daftarKamar, riwayatPemesanan
    # Kalau file belum ada, biarkan data awal di atas (try-except FileNotFoundError)
    pass


def simpanData():
    # TODO: tulis dataPengguna, daftarKamar, riwayatPemesanan ke namaFile (JSON)
    pass