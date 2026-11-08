import json

namaFile = "dataKosku.json"

tipeKamar = ("Standar", "Deluxe", "VIP")

dataPengguna = {
    "shean": {"password": "059", "level": "admin", "saldo": 0, "kamarSewa": None},
    "robin": {"password": "068", "level": "admin", "saldo": 0, "kamarSewa": None},
    "alfi": {"password": "056", "level": "user", "saldo": 3000000, "kamarSewa": None},
}


daftarKamar = {
    "K001": {"tipe": "Standar", "harga": 750000, "fasilitas": "Kipas angin, Kasur, KM luar", "status": "Kosong", "penyewa": None},
    "K002": {"tipe": "Standar", "harga": 950000, "fasilitas": "Kipas angin, Kasur, KM dalam", "status": "Terisi", "penyewa": alfi},
    "K003": {"tipe": "Deluxe", "harga": 1500000, "fasilitas": "AC, Kasur, KM dalam, WiFi, Meja belajar, Balkon", "status": "Kosong", "penyewa": None},
    "K004": {"tipe": "Deluxe", "harga": 1800000, "fasilitas": "AC, Kasur, KM dalam, WiFi, Lemari, Balkon", "status": "Kosong", "penyewa": None},
    "K005": {"tipe": "VIP", "harga": 2500000, "fasilitas": "AC, Kasur, KM dalam, WiFi, Lemari, Balkon, Smart TV, Kulkas mini", "status": "Kosong", "penyewa": None},
}


riwayatPemesanan = {
    "username": "alfi", "idKamar": "K002", "harga": 950000, "tanggal": "2026-08-01 10:30:00"
}


sesi = {"penggunaLogin": None}


def muatData():
    global dataPengguna, daftarKamar, riwayatPemesanan
    try:
        with open(namaFile, "r", encoding="utf-8") as f:
            data = json.load(f)
            dataPengguna = data.get("dataPengguna", dataPengguna)
            daftarKamar = data.get("daftarKamar", daftarKamar)
            riwayatPemesanan = data.get("riwayatPemesanan", riwayatPemesanan)
    except FileNotFoundError:
        pass


def simpanData():
    data = {
        "dataPengguna": dataPengguna,
        "daftarKamar": daftarKamar,
        "riwayatPemesanan": riwayatPemesanan,
    }
    with open(namaFile, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)