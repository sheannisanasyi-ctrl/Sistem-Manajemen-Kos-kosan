from prettytable import PrettyTable, ALL
from data import daftarKamar, tipeKamar, hargaMinimal
from utils import (bersihkanLayar, tekanEnter, validasiAngka, generateIdBaru,
                   formatRupiah, pilihMenu, tampilHeader)


def inputHarga(teks, tipe):
    minimal = hargaMinimal[tipe]
    harga = input(f"{teks} (minimal {formatRupiah(minimal)}): ").strip()
    if harga == "":
        print("(!_!) Harga tidak boleh kosong!")
        return None
    if not validasiAngka(harga):
        print("(!_!) Harga harus berupa angka bulat tanpa titik atau huruf, contoh: 750000")
        return None
    harga = int(harga)
    if harga < minimal:
        print(f"Harga kamar {tipe} minimal {formatRupiah(minimal)}")
        return None
    return harga


def inputFasilitas(teks):
    fasilitas = input(teks).strip()

    # set menyimpan nama fasilitas yang sudah muncul, supaya tidak ada yang ganda
    sudahAda = set()
    daftarBersih = []
    for item in fasilitas.split(","):
        item = item.strip()
        if item != "" and item.lower() not in sudahAda:
            sudahAda.add(item.lower())
            daftarBersih.append(item)

    if len(daftarBersih) == 0:
        print("(!_!) Fasilitas tidak boleh kosong")
        return None
    return ", ".join(daftarBersih)


def kelolaKamar():
    while True:
        bersihkanLayar()
        tampilHeader("KELOLA KAMAR")
        pilihan = pilihMenu(
            "Kelola Kamar",
            ["Tambah", "Lihat", "Ubah", "Hapus", "Kembali"],
        )

        if pilihan == "Tambah":
            tambahKamar()
            tekanEnter()
        elif pilihan == "Lihat":
            bersihkanLayar()
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
    tampilHeader("TAMBAH KAMAR")
    idBaru = generateIdBaru()

    tipe = pilihMenu("Pilih tipe kamar", list(tipeKamar))
    if tipe not in tipeKamar:
        print("Tipe kamar tidak valid")
        return

    harga = inputHarga("Masukkan harga kamar", tipe)
    if harga is None:
        return

    fasilitas = inputFasilitas("Masukkan fasilitas kamar: ")
    if fasilitas is None:
        return

    daftarKamar[idBaru] = {
        "tipe": tipe,
        "harga": harga,
        "fasilitas": fasilitas,
        "status": "Kosong",
        "penyewa": None,
    }
    print(f"\nKamar {idBaru} berhasil ditambahkan!")


def lihatKamar(hanyaKosong=False):
    if not daftarKamar:
        print("Belum ada data kamar")
        return

    tabel = PrettyTable()
    tabel.title = "DAFTAR KAMAR KOSONG" if hanyaKosong else "DATA KAMAR"
    tabel.align = "c"
    tabel.hrules = ALL

    if hanyaKosong:
        tabel.field_names = ["ID", "Tipe", "Harga", "Fasilitas"]
        tabel.max_width = {"Fasilitas": 30}
    else:
        tabel.field_names = ["ID", "Tipe", "Harga", "Fasilitas", "Status", "Penyewa"]
        tabel.max_width = {"Fasilitas": 30}

    jumlahBaris = 0
    for idKamar, kamar in daftarKamar.items():
        if hanyaKosong and kamar["status"] != "Kosong":
            continue

        harga = formatRupiah(int(kamar["harga"]))
        if hanyaKosong:
            tabel.add_row([idKamar, kamar["tipe"], harga, kamar["fasilitas"]])
        else:
            penyewa = kamar["penyewa"]
            if penyewa is None:
                penyewa = "-"
            tabel.add_row([idKamar, kamar["tipe"], harga, kamar["fasilitas"], kamar["status"], penyewa])

        jumlahBaris += 1

    if jumlahBaris > 0:
        print(tabel)
    else:
        print("Tidak ada kamar kosong!")


def inputIdKamar():
    idKamar = input("Masukkan ID kamar: ").upper().strip()
    if idKamar == "":
        print("(!_!) ID kamar tidak boleh kosong!")
        return None
    if idKamar not in daftarKamar:
        print("(!_!) ID kamar tidak ditemukan!")
        return None
    return idKamar


def ubahKamar():
    bersihkanLayar()
    tampilHeader("UBAH KAMAR")
    lihatKamar()
    idKamar = inputIdKamar()
    if idKamar is None:
        return

    pilihan = pilihMenu("Bagian yang diubah", ["Tipe", "Harga", "Fasilitas", "Semua", "Batal"])

    if pilihan == "Tipe":
        ubahTipe(idKamar)
    elif pilihan == "Harga":
        ubahHarga(idKamar)
    elif pilihan == "Fasilitas":
        ubahFasilitas(idKamar)
    elif pilihan == "Semua":
        tipeLama = daftarKamar[idKamar]["tipe"]
        if ubahTipe(idKamar, False):
            if ubahHarga(idKamar):
                ubahFasilitas(idKamar)
            else:
                daftarKamar[idKamar]["tipe"] = tipeLama
                print("Perubahan tipe dibatalkan")
    else:
        print("Perubahan dibatalkan")


def ubahTipe(idKamar, cekHarga=True):
    pilihan = pilihMenu("Pilih tipe baru", list(tipeKamar))
    if pilihan not in tipeKamar:
        print("(!_!) Tipe kamar tidak valid!")
        return False
    if cekHarga and daftarKamar[idKamar]["harga"] < hargaMinimal[pilihan]:
        print(f"Harga kamar saat ini di bawah minimal tipe {pilihan} "
              f"({formatRupiah(hargaMinimal[pilihan])}). Ubah harga lebih dulu atau pilih 'Semua'.")
        return False
    daftarKamar[idKamar]["tipe"] = pilihan
    print("Tipe berhasil diubah")
    return True


def ubahHarga(idKamar):
    harga = inputHarga("Masukkan harga baru", daftarKamar[idKamar]["tipe"])
    if harga is None:
        return False
    daftarKamar[idKamar]["harga"] = harga
    print("Harga berhasil diubah")
    return True


def ubahFasilitas(idKamar):
    fasilitas = inputFasilitas("Masukkan fasilitas baru: ")
    if fasilitas is None:
        return False
    daftarKamar[idKamar]["fasilitas"] = fasilitas
    print("Fasilitas berhasil diubah!")
    return True


def hapusKamar():
    bersihkanLayar()
    tampilHeader("HAPUS KAMAR")
    lihatKamar()
    idKamar = inputIdKamar()
    if idKamar is None:
        return

    if daftarKamar[idKamar]["status"] == "Terisi":
        print("Kamar sedang disewa, tidak bisa dihapus!")
        return

    konfirmasi = pilihMenu(
        f"Yakin ingin menghapus kamar {idKamar}?",
        ["Ya, hapus", "Tidak jadi"],
    )
    if konfirmasi == "Ya, hapus":
        del daftarKamar[idKamar]
        print("Kamar berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")