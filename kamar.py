from data import daftarKamar, riwayatPemesanan, tipeKamar, hargaMinimal, maksHarga, simpanData
from utils import (tekanEnter, siapkanLayar, validasiAngka, formatRupiah,
                   pilihMenu, buatTabel, pesanSukses, pesanPeringatan, pesanGagal)

maksFasilitas = 100


def generateIdBaru():
    terpakai = set(daftarKamar) | {item["idKamar"] for item in riwayatPemesanan}
    nomor = 1
    while f"K{nomor:03d}" in terpakai:
        nomor += 1
    return f"K{nomor:03d}"


def inputHarga(pesan, tipe):
    minimal = hargaMinimal[tipe]
    harga = input(f"{pesan} (minimal {formatRupiah(minimal)}): ").strip()
    if harga == "":
        pesanPeringatan("Harga jangan dikosongin dong!")
        return None
    if harga.startswith("-") and validasiAngka(harga[1:]):
        pesanPeringatan("Harga nggak boleh negatif ya!")
        return None
    if not validasiAngka(harga):
        pesanPeringatan("Harga harus angka bulat tanpa titik atau huruf ya, contoh: 750000")
        return None
    harga = int(harga)
    if harga < minimal:
        pesanPeringatan(f"Harga kamar {tipe} minimal {formatRupiah(minimal)} ya!")
        return None
    if harga > maksHarga:
        pesanPeringatan(f"Kemahalan! Harga kamar maksimal {formatRupiah(maksHarga)} ya!")
        return None
    return harga


def inputFasilitas(pesan):
    fasilitas = input(pesan).strip()
    sudahAda = set()
    daftarBersih = []
    for item in fasilitas.split(","):
        item = item.strip()
        if item != "" and item.lower() not in sudahAda:
            sudahAda.add(item.lower())
            daftarBersih.append(item)
    if len(daftarBersih) == 0:
        pesanPeringatan("Fasilitas jangan dikosongin dong!")
        return None
    hasil = ", ".join(daftarBersih)
    if len(hasil) > maksFasilitas:
        pesanPeringatan(f"Fasilitasnya kepanjangan, maksimal {maksFasilitas} karakter ya!")
        return None
    return hasil


def inputIdKamar():
    idKamar = input("Masukkan ID kamar: ").strip().upper()
    if idKamar == "":
        pesanPeringatan("ID kamar jangan dikosongin dong!")
        return None
    if idKamar not in daftarKamar:
        pesanGagal("ID kamar nggak ketemu nih!")
        return None
    return idKamar


def pilihTipe(judul):
    tipe = pilihMenu(judul, list(tipeKamar))
    if tipe not in tipeKamar:
        pesanPeringatan("Tipe kamar belum dipilih nih!")
        return None
    return tipe


def kelolaKamar():
    while True:
        siapkanLayar("KELOLA KAMAR")
        pilihan = pilihMenu("Kelola Kamar", ["Tambah", "Lihat", "Ubah", "Hapus", "Kembali"])

        if pilihan == "Tambah":
            siapkanLayar("TAMBAH KAMAR")
            if tambahKamar():
                simpanData()
            tekanEnter()
        elif pilihan == "Lihat":
            siapkanLayar("DATA KAMAR")
            lihatKamar()
            tekanEnter()
        elif pilihan == "Ubah":
            siapkanLayar("UBAH KAMAR")
            if ubahKamar():
                simpanData()
            tekanEnter()
        elif pilihan == "Hapus":
            siapkanLayar("HAPUS KAMAR")
            if hapusKamar():
                simpanData()
            tekanEnter()
        else:
            break


def tambahKamar():
    tipe = pilihTipe("Pilih tipe kamar")
    if tipe is None:
        return False
    harga = inputHarga("Masukkan harga kamar", tipe)
    if harga is None:
        return False
    fasilitas = inputFasilitas("Masukkan fasilitas kamar (pisahkan dengan koma): ")
    if fasilitas is None:
        return False

    idBaru = generateIdBaru()
    daftarKamar[idBaru] = {
        "tipe": tipe,
        "harga": harga,
        "fasilitas": fasilitas,
        "status": "Kosong",
        "penyewa": None,
    }
    pesanSukses(f"YEAY! Kamar {idBaru} berhasil ditambahkan!")
    return True


def lihatKamar(hanyaKosong=False):
    if not daftarKamar:
        pesanPeringatan("Belum ada data kamar nih!")
        return

    if hanyaKosong:
        tabel = buatTabel("DAFTAR KAMAR KOSONG", ["ID", "Tipe", "Harga", "Fasilitas"])
    else:
        tabel = buatTabel("DATA KAMAR", ["ID", "Tipe", "Harga", "Fasilitas", "Status", "Penyewa"])
    tabel.max_width = 30

    jumlahBaris = 0
    for idKamar, kamar in sorted(daftarKamar.items()):
        if hanyaKosong and kamar["status"] != "Kosong":
            continue
        harga = formatRupiah(int(kamar["harga"]))
        if hanyaKosong:
            tabel.add_row([idKamar, kamar["tipe"], harga, kamar["fasilitas"]])
        else:
            penyewa = kamar["penyewa"] if kamar["penyewa"] is not None else "-"
            tabel.add_row([idKamar, kamar["tipe"], harga, kamar["fasilitas"], kamar["status"], penyewa])
        jumlahBaris += 1

    if jumlahBaris > 0:
        print(tabel)
    else:
        pesanPeringatan("Yah, nggak ada kamar kosong!")


def ubahKamar():
    lihatKamar()
    if not daftarKamar:
        return False
    idKamar = inputIdKamar()
    if idKamar is None:
        return False
    kamar = daftarKamar[idKamar]

    pilihan = pilihMenu("Bagian yang diubah", ["Tipe", "Harga", "Fasilitas", "Semua", "Batal"])

    if pilihan == "Tipe":
        tipeBaru = pilihTipe("Pilih tipe baru")
        if tipeBaru is None:
            return False
        if kamar["harga"] < hargaMinimal[tipeBaru]:
            pesanGagal(f"Harga kamar saat ini di bawah minimal tipe {tipeBaru} "
                       f"({formatRupiah(hargaMinimal[tipeBaru])}). Ubah harga dulu atau pilih 'Semua' ya!")
            return False
        kamar["tipe"] = tipeBaru
        pesanSukses("YEAY! Tipe berhasil diubah!")
        return True

    if pilihan == "Harga":
        harga = inputHarga("Masukkan harga baru", kamar["tipe"])
        if harga is None:
            return False
        kamar["harga"] = harga
        pesanSukses("YEAY! Harga berhasil diubah!")
        return True

    if pilihan == "Fasilitas":
        fasilitas = inputFasilitas("Masukkan fasilitas baru (pisahkan dengan koma): ")
        if fasilitas is None:
            return False
        kamar["fasilitas"] = fasilitas
        pesanSukses("YEAY! Fasilitas berhasil diubah!")
        return True

    if pilihan == "Semua":
        tipeBaru = pilihTipe("Pilih tipe baru")
        harga = inputHarga("Masukkan harga baru", tipeBaru) if tipeBaru else None
        fasilitas = (inputFasilitas("Masukkan fasilitas baru (pisahkan dengan koma): ")
                     if harga is not None else None)
        if tipeBaru is None or harga is None or fasilitas is None:
            pesanPeringatan("Perubahan dibatalkan, data kamar nggak ada yang berubah!")
            return False
        kamar["tipe"] = tipeBaru
        kamar["harga"] = harga
        kamar["fasilitas"] = fasilitas
        pesanSukses("YEAY! Semua data kamar berhasil diubah!")
        return True

    pesanPeringatan("Batal ubah kamar, nggak ada yang berubah!")
    return False


def hapusKamar():
    lihatKamar()
    if not daftarKamar:
        return False
    idKamar = inputIdKamar()
    if idKamar is None:
        return False
    if daftarKamar[idKamar]["status"] == "Terisi":
        pesanGagal("Kamar lagi disewa, nggak bisa dihapus!")
        return False

    konfirmasi = pilihMenu(f"Yakin mau hapus kamar {idKamar}?", ["Ya, hapus", "Tidak jadi"])
    if konfirmasi == "Ya, hapus":
        del daftarKamar[idKamar]
        pesanSukses("YEAY! Kamar berhasil dihapus!")
        return True
    pesanPeringatan("Penghapusan dibatalkan!")
    return False