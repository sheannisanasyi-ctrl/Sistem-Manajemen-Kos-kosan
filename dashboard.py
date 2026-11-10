# dashboard.py - ringkasan untuk admin (Orang 3)

from prettytable import PrettyTable
from data import dataPengguna, daftarKamar, riwayatPemesanan, tipeKamar
from utils import formatRupiah


def tampilDashboard():
    # TODO: sesuai flowchart tampilDashboard()
    # - totalKamar = len(daftarKamar)
    # - kamarTerisi: perulangan for atas daftarKamar.values(), hitung status "Terisi"
    # - kamarKosong = totalKamar - kamarTerisi
    # - okupansi pakai ternary + round (modul 3):
    #   okupansi = round(kamarTerisi / totalKamar * 100, 1) if totalKamar > 0 else 0
    # - totalPendapatan: perulangan for atas riwayatPemesanan, jumlahkan "harga"
    # - totalUser: jumlah akun di dataPengguna yang levelnya "user"
    # - penyewaUnik = len(set(...username dari riwayatPemesanan...))  (set menghilangkan duplikasi)
    # - tampilkan ringkasan (formatRupiah untuk pendapatan)
    # - lalu panggil rekapPerTipe() dan pemesananTerbaru()
    pass


def rekapPerTipe():
    # TODO: sesuai flowchart rekapPerTipe(), memakai NESTED FOR
    # - tabel PrettyTable: Tipe, Kosong, Terisi
    # - for tipe in tipeKamar:  (perulangan luar)
    #       kosong = 0, terisi = 0
    #       for kamar in daftarKamar.values():  (perulangan dalam)
    #           jika tipe kamar bukan tipe saat ini: continue
    #           hitung kosong atau terisi
    #       tambah baris ke tabel
    pass


def pemesananTerbaru():
    # TODO: sesuai flowchart pemesananTerbaru(), memakai range(start, stop, step) dan break
    # - jika riwayat kosong: "Belum ada pemesanan"
    # - for i in range(len(riwayatPemesanan) - 1, -1, -1):  (dari yang terakhir, mundur)
    #       tambah baris ke tabel (username, idKamar, harga, tanggal)
    #       jika sudah 5 baris: break
    pass