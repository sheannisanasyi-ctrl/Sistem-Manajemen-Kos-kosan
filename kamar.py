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
    # - lihatKamar(), input ID kamar, cek ID ada
    # - input tipe, harga, fasilitas baru (kosong = tidak diubah)
    # - JANGAN ubah status/penyewa di sini (status hanya berubah lewat pesanKamar dan berhentiSewa)
    # - harga yang diisi harus valid, tipe yang diisi harus ada di tipeKamar
    pass


def hapusKamar():
    # TODO: sesuai flowchart hapusKamar()
    # - lihatKamar(), input ID kamar, cek ID ada
    # - status "Terisi": tidak boleh dihapus
    # - konfirmasi y/n sebelum hapus
    pass