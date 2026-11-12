# kamar.py - CRUD kamar (Orang 2)

from prettytable import PrettyTable
from data import daftarKamar, tipeKamar 
from utils import bersihkanLayar, tekanEnter, validasiAngka, generateIdBaru, formatRupiah, pilihMenu


def kelolaKamar():
    while True:
        bersihkanLayar()
        print("=" * 40)
        print("  KELOLA KAMAR")
        print("=" * 40)
        pilihan = pilihMenu(
            "Kelola Kamar",
            ["Tambah", "Lihat", "Ubah", "Hapus", "Kembali"],
        )

        if pilihan == "Tambah":
            tambahKamar()
            tekanEnter()
        elif pilihan == "Lihat":
            lihatKamar()
            tekanEnter()
        elif pilihan == "Ubah":
            ubahKamar()
            tekanEnter()
        elif pilihan == "Hapus":
            hapusKamar()
            tekanEnter()
        else:
            break
    # TODO: while True, tampilkan submenu dengan pilihMenu("Kelola Kamar", [...])
    # Pilihan: "Tambah", "Lihat", "Ubah", "Hapus", "Kembali"
    # - panggil fungsi yang sesuai, lalu tekanEnter() (karena menu ini punya perulangan sendiri)
    # - "Kembali" (atau None jika Ctrl+C): break


def tambahKamar():
    bersihkanLayar()
    idBaru = generateIdBaru()

    tipe = pilihMenu("Pilih tipe kamar", list(tipeKamar))

    if tipe not in tipeKamar:
        print("Tipe kamar tidak valid")
        return
    
    angka = int(input("Masukkan harga kamar: "))

    if not validasiAngka(str(angka)):
        print("Harga harus angka lebih dari 0")
        return

    fasilitas = input("Masukkan fasilitas kamar: ")

    daftarKamar[idBaru] = {
        "tipe": tipe,
        "harga": angka,
        "fasilitas": fasilitas,
        "status": "Kosong",
        "penyewa": None
    }
    print("\nKamar berhasil ditambahkan")
    # TODO: sesuai flowchart tambahKamar()
    # - idBaru = generateIdBaru()
    # - input tipe, harga, fasilitas
    # - tipe harus ada di tipeKamar (tuple)
    # - harga harus validasiAngka() lalu diubah ke int
    # - simpan: {"tipe", "harga", "fasilitas", "status": "Kosong", "penyewa": None}


def lihatKamar(hanyaKosong=False):
    bersihkanLayar()
    if not daftarKamar:
        print("Belum ada data kamar")
        return

    tabel = PrettyTable()
    tabel.align = "l"
    if hanyaKosong:
        tabel.field_names = ["ID", "Tipe", "Harga", "Fasilitas"]
    else:
        tabel.field_names = ["ID", "Tipe", "Harga", "Fasilitas", "Status", "Penyewa"]

    jumlahBaris = 0
    for idKamar, kamar in daftarKamar.items():
        if hanyaKosong and kamar["status"] != "Kosong":
            continue

        if hanyaKosong:
            tabel.add_row([idKamar, kamar["tipe"], formatRupiah(int(kamar["harga"])), kamar["fasilitas"]])
        else:
            penyewa = kamar["penyewa"] 

            if kamar["penyewa"] is None:
                penyewa = "-"
            
            tabel.add_row([idKamar, kamar["tipe"], formatRupiah(int(kamar["harga"])), kamar["fasilitas"], kamar["status"], penyewa])

        jumlahBaris += 1

    if jumlahBaris > 0:
        print(tabel)
    else:
        print("Tidak ada kamar kosong")

    # TODO: sesuai flowchart lihatKamar()
    # - jika daftarKamar kosong: "Belum ada data kamar"
    # - hanyaKosong True (tampilan user): kolom ID, Tipe, Harga (formatRupiah), Fasilitas
    # - hanyaKosong False (tampilan admin): kolom ID, Tipe, Harga, Fasilitas, Status, Penyewa
    #   (isi nama penyewa, atau "-" jika penyewa None)
    # - jumlahBaris = 0
    # - for idKamar, kamar in daftarKamar.items():
    #       hanyaKosong True dan status bukan "Kosong": continue
    #       tambah baris ke tabel (sesuai kolom), jumlahBaris += 1
    # - jumlahBaris > 0: tampilkan tabel; selain itu: "Tidak ada kamar kosong"



def ubahKamar():
    bersihkanLayar()
    lihatKamar()
    idKamar = input("Masukkan ID kamar: ").upper().strip()

    if idKamar not in daftarKamar:
        print("ID kamar tidak ditemukan")
        return

    pilihan = pilihMenu("Bagian yang diubah", ["Tipe", "Harga", "Fasilitas", "Semua", "Batal"])

    if pilihan == "Tipe":
        ubahTipe(idKamar)
    elif pilihan == "Harga":
        ubahHarga(idKamar)
    elif pilihan == "Fasilitas":
        ubahFasilitas(idKamar)
    elif pilihan == "Semua":
        ubahTipe(idKamar)
        ubahHarga(idKamar)
        ubahFasilitas(idKamar)
    else:
        print("Perubahan dibatalkan")
    # TODO: sesuai flowchart ubahKamar()
    # - lihatKamar(), input ID kamar, cek ID ada (jika tidak: "ID tidak ditemukan", selesai)
    # - pilihan = pilihMenu("Bagian yang diubah", ["Tipe", "Harga", "Fasilitas", "Semua", "Batal"])
    # - "Tipe": ubahTipe(idKamar)
    #   "Harga": ubahHarga(idKamar)
    #   "Fasilitas": ubahFasilitas(idKamar)
    #   "Semua": ubahTipe(idKamar), ubahHarga(idKamar), lalu ubahFasilitas(idKamar)
    #   selain itu ("Batal" atau None jika Ctrl+C): "Perubahan dibatalkan"
    # - JANGAN ubah status/penyewa di sini (status hanya berubah lewat pesanKamar dan berhentiSewa)


def ubahTipe(idKamar):
    pilihan = pilihMenu("Pilih tipe baru", list(tipeKamar))
    daftarKamar[idKamar]["tipe"] = pilihan
    print("Tipe berhasil diubah")

    # TODO: sesuai flowchart ubahTipe(idKamar)
    # - pilih tipe baru dari menu: pilihMenu("Tipe baru", list(tipeKamar))
    #   (karena dipilih dari tipeKamar, tipenya pasti valid)
    # - daftarKamar[idKamar]["tipe"] = tipe baru, tampilkan "Tipe berhasil diubah"


def ubahHarga(idKamar):
    pilihan = int(input("Masukkan harga baru: "))
    if validasiAngka(str(pilihan)):
        daftarKamar[idKamar]["harga"] = pilihan
        print("Harga berhasil diubah")
    else:
        print("Harga harus angka lebih dari 0")
    # TODO: sesuai flowchart ubahHarga(idKamar)
    # - input harga baru, harus validasiAngka() (angka lebih dari 0), lalu diubah ke int
    # - daftarKamar[idKamar]["harga"] = harga baru, tampilkan "Harga berhasil diubah"
    # - jika tidak valid: "Harga harus angka lebih dari 0"


def ubahFasilitas(idKamar):
    pilihan = input("Masukkan fasilitas baru: ")
    if pilihan == "":
        print("Fasilitas tidak boleh kosong")
    else:
        daftarKamar[idKamar]["fasilitas"] = pilihan
        print("Fasilitas berhasil diubah")
    # TODO: sesuai flowchart ubahFasilitas(idKamar)
    # - input fasilitas baru, tidak boleh kosong
    # - daftarKamar[idKamar]["fasilitas"] = fasilitas baru, tampilkan "Fasilitas berhasil diubah"


def hapusKamar():
    bersihkanLayar()
    lihatKamar()
    idKamar = input("Masukkan ID kamar: ").upper().strip()

    if idKamar not in daftarKamar:
        print("ID kamar tidak ditemukan")
        return
    else:
        if daftarKamar[idKamar]["status"] == "Terisi":
            print("Kamar sedang disewa, tidak bisa dihapus")
            return
        else:
            konfirmasi = input("Apakah Anda yakin ingin menghapus kamar ini? (y/n): ").lower().strip()
            if konfirmasi == "y":
                del daftarKamar[idKamar]
                print("Kamar berhasil dihapus")
            else:
                print("Penghapusan dibatalkan")
    # TODO: sesuai flowchart hapusKamar()
    # - lihatKamar(), input ID kamar, cek ID ada
    # - status "Terisi": tidak boleh dihapus
    # - konfirmasi y/n sebelum hapus