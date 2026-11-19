import json

namaFile = "dataKosku.json"

tipeKamar = ("Standar", "Deluxe", "VIP")
hargaMinimal = {"Standar": 500000, "Deluxe": 1000000, "VIP": 2000000}

dataPengguna = {
    "shean": {"password": "059", "level": "admin", "saldo": 0, "kamarSewa": None},
    "robin": {"password": "068", "level": "admin", "saldo": 0, "kamarSewa": None},
    "alfi": {"password": "056", "level": "user", "saldo": 3000000, "kamarSewa": "K002"},
    "novi": {"password": "111", "level": "user", "saldo": 1200000, "kamarSewa": "K004"},
    "aldi": {"password": "222", "level": "user", "saldo": 500000, "kamarSewa": "K007"},
    "budi": {"password": "123", "level": "user", "saldo": 2000000, "kamarSewa": None},
    "eka": {"password": "333", "level": "user", "saldo": 500000, "kamarSewa": None},
}


daftarKamar = {
    "K001": {"tipe": "Standar", "harga": 750000, "fasilitas": "Kipas angin, Kasur, KM luar", "status": "Kosong", "penyewa": None},
    "K002": {"tipe": "Standar", "harga": 950000, "fasilitas": "Kipas angin, Kasur, KM dalam", "status": "Terisi", "penyewa": "alfi"},
    "K003": {"tipe": "Standar", "harga": 850000, "fasilitas": "Kipas angin, Kasur, Lemari, KM luar", "status": "Kosong", "penyewa": None},
    "K004": {"tipe": "Deluxe", "harga": 1500000, "fasilitas": "AC, Kasur, KM dalam, WiFi, Meja belajar", "status": "Terisi", "penyewa": "novi"},
    "K005": {"tipe": "Deluxe", "harga": 1800000, "fasilitas": "AC, Kasur, KM dalam, WiFi, Lemari, Balkon", "status": "Kosong", "penyewa": None},
    "K006": {"tipe": "Deluxe", "harga": 1650000, "fasilitas": "AC, Kasur, KM dalam, WiFi, Lemari", "status": "Kosong", "penyewa": None},
    "K007": {"tipe": "VIP", "harga": 2500000, "fasilitas": "AC, Kasur, KM dalam, WiFi, Lemari, Balkon, Smart TV, Kulkas mini", "status": "Terisi", "penyewa": "aldi"},
    "K008": {"tipe": "VIP", "harga": 2800000, "fasilitas": "AC, Kasur king, KM dalam, WiFi, Lemari, Balkon, Smart TV, Kulkas mini, Dapur kecil", "status": "Kosong", "penyewa": None},
}


riwayatPemesanan = [
    {"username": "alfi", "idKamar": "K002", "harga": 950000, "tanggal": "2026-08-01 10:30:00"},
    {"username": "novi", "idKamar": "K004", "harga": 1500000, "tanggal": "2026-08-15 14:05:00"},
    {"username": "budi", "idKamar": "K001", "harga": 750000, "tanggal": "2026-09-03 09:12:00"},
    {"username": "aldi", "idKamar": "K007", "harga": 2500000, "tanggal": "2026-10-05 16:40:00"},
    {"username": "eka", "idKamar": "K003", "harga": 850000, "tanggal": "2026-10-20 11:20:00"},
]


sesi = {"penggunaLogin": None}


def muatData():
    try:
        with open(namaFile, "r", encoding="utf-8") as f:
            data = json.load(f)
        dataPengguna.clear()
        dataPengguna.update(data.get("dataPengguna", {}))
        daftarKamar.clear()
        daftarKamar.update(data.get("daftarKamar", {}))
        riwayatPemesanan.clear()
        riwayatPemesanan.extend(data.get("riwayatPemesanan", []))
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        print("File data rusak, memakai data awal.")


def simpanData():
    data = {
        "dataPengguna": dataPengguna,
        "daftarKamar": daftarKamar,
        "riwayatPemesanan": riwayatPemesanan,
    }
    with open(namaFile, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)