from prettytable import PrettyTable, ALL
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

    fasilitas = input("Masukkan fasilitas kamar: ").strip()

    daftarKamar[idBaru] = {
        "tipe": tipe,
        "harga": angka,
        "fasilitas": fasilitas,
        "status": "Kosong",
        "penyewa": None
    }
    print("\nKamar berhasil ditambahkan")


def lihatKamar(hanyaKosong=False):
    bersihkanLayar()
    if not daftarKamar:
        print("Belum ada data kamar")
        return

    tabel = PrettyTable()
    tabel.align = "c"
    tabel.hrules = ALL

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
 

def ubahTipe(idKamar):
    pilihan = pilihMenu("Pilih tipe baru", list(tipeKamar))
    daftarKamar[idKamar]["tipe"] = pilihan
    print("Tipe berhasil diubah")


def ubahHarga(idKamar):
    pilihan = int(input("Masukkan harga baru: "))
    if validasiAngka(str(pilihan)):
        daftarKamar[idKamar]["harga"] = pilihan
        print("Harga berhasil diubah")
    else:
        print("Harga harus angka lebih dari 0")
  

def ubahFasilitas(idKamar):
    pilihan = input("Masukkan fasilitas baru: ").strip()
    if pilihan == "":
        print("Fasilitas tidak boleh kosong")
    else:
        daftarKamar[idKamar]["fasilitas"] = pilihan
        print("Fasilitas berhasil diubah")
   

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