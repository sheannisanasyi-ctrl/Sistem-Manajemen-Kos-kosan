# kamar.py - CRUD kamar (Orang 2)

from data import daftarKamar, tipeKamar
from utils import generateIdBaru, validasiAngka


def kelolaKamar():
    # TODO: submenu while True: 1 Tambah, 2 Lihat, 3 Ubah, 4 Hapus, 5 Kembali
    pass


def tambahKamar():
    # TODO: input tipe, harga, fasilitas
    # - tipe harus ada di tipeKamar (tuple)
    # - harga angka > 0
    # - ID dari generateIdBaru(), status awal "Kosong", penyewa None
    pass


def lihatKamar(hanyaKosong=False):
    # TODO: tampilkan tabel PrettyTable (ID, Tipe, Harga, Fasilitas, Status)
    # - hanyaKosong True: tampilkan kamar berstatus "Kosong" saja (dipakai user)
    # - jika data kosong: tampilkan "Belum ada data kamar"
    pass


def ubahKamar():
    # TODO: tampilkan tabel, input ID kamar
    # - ID tidak ada: pesan error
    # - input data baru, kosong = tidak diubah
    # - harga yang diisi harus valid
    pass


def hapusKamar():
    # TODO: tampilkan tabel, input ID kamar
    # - ID tidak ada: pesan error
    # - status "Terisi": tidak boleh dihapus
    # - konfirmasi y/n sebelum hapus
    pass