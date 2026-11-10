# kamar.py - CRUD kamar (Orang 2)

from prettytable import PrettyTable
from data import daftarKamar, tipeKamar
from utils import bersihkanLayar, tekanEnter, validasiAngka, generateIdBaru, formatRupiah, pilihMenu


def kelolaKamar():
    # TODO: while True, tampilkan submenu dengan pilihMenu("Kelola Kamar", [...])
    # Pilihan: "Tambah", "Lihat", "Ubah", "Hapus", "Kembali"
    # - panggil fungsi yang sesuai, lalu tekanEnter() (karena menu ini punya perulangan sendiri)
    # - "Kembali" (atau None jika Ctrl+C): break
    pass


def tambahKamar():
    # TODO: sesuai flowchart tambahKamar()
    # - idBaru = generateIdBaru()
    # - input tipe, harga, fasilitas
    # - tipe harus ada di tipeKamar (tuple)
    # - harga harus validasiAngka() lalu diubah ke int
    # - simpan: {"tipe", "harga", "fasilitas", "status": "Kosong", "penyewa": None}
    pass


def lihatKamar(hanyaKosong=False):
    # TODO: sesuai flowchart lihatKamar()
    # - jika daftarKamar kosong: "Belum ada data kamar"
    # - tabel PrettyTable: ID, Tipe, Harga (formatRupiah), Fasilitas, Status
    # - for idKamar, kamar in daftarKamar.items():
    #       hanyaKosong True dan status bukan "Kosong": continue
    #       tambah baris ke tabel
    pass


def ubahKamar():
    # TODO: sesuai flowchart ubahKamar()
    # - lihatKamar(), input ID kamar, cek ID ada (jika tidak: "ID tidak ditemukan", selesai)
    # - pilihan = pilihMenu("Bagian yang diubah", ["Tipe", "Harga", "Fasilitas", "Semua", "Batal"])
    # - "Tipe": ubahTipe(idKamar)
    #   "Harga": ubahHarga(idKamar)
    #   "Fasilitas": ubahFasilitas(idKamar)
    #   "Semua": ubahTipe(idKamar), ubahHarga(idKamar), lalu ubahFasilitas(idKamar)
    #   selain itu ("Batal" atau None jika Ctrl+C): "Perubahan dibatalkan"
    # - JANGAN ubah status/penyewa di sini (status hanya berubah lewat pesanKamar dan berhentiSewa)
    pass


def ubahTipe(idKamar):
    # TODO: sesuai flowchart ubahTipe(idKamar)
    # - pilih tipe baru dari menu: pilihMenu("Tipe baru", list(tipeKamar))
    #   (karena dipilih dari tipeKamar, tipenya pasti valid)
    # - daftarKamar[idKamar]["tipe"] = tipe baru, tampilkan "Tipe berhasil diubah"
    pass


def ubahHarga(idKamar):
    # TODO: sesuai flowchart ubahHarga(idKamar)
    # - input harga baru, harus validasiAngka() (angka lebih dari 0), lalu diubah ke int
    # - daftarKamar[idKamar]["harga"] = harga baru, tampilkan "Harga berhasil diubah"
    # - jika tidak valid: "Harga harus angka lebih dari 0"
    pass


def ubahFasilitas(idKamar):
    # TODO: sesuai flowchart ubahFasilitas(idKamar)
    # - input fasilitas baru, tidak boleh kosong
    # - daftarKamar[idKamar]["fasilitas"] = fasilitas baru, tampilkan "Fasilitas berhasil diubah"
    pass


def hapusKamar():
    # TODO: sesuai flowchart hapusKamar()
    # - lihatKamar(), input ID kamar, cek ID ada
    # - status "Terisi": tidak boleh dihapus
    # - konfirmasi y/n sebelum hapus
    pass