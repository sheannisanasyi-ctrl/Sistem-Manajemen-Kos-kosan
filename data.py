import json
import os
import time

from keamanan import hashPassword, sudahDihash
from utils import pesanGagal

namaFile = "dataKosku.json"
tipeKamar = ("Standar", "Deluxe", "VIP")
hargaMinimal = {"Standar": 500000, "Deluxe": 1000000, "VIP": 2000000}
maksHarga = 50_000_000
maksTopup = 100_000_000

dataPengguna = {}
daftarKamar = {}
riwayatPemesanan = []
sesi = {"penggunaLogin": None, "terkunciSampai": 0}

kunciAkun = {"password", "level", "saldo", "kamarSewa"}
kunciKamar = {"tipe", "harga", "fasilitas", "status", "penyewa"}
kunciRiwayat = {"username", "idKamar", "harga", "tanggal"}


def isiDataAwal():
    akunAwal = [
        ("shean", "059", "admin", 0, None),
        ("robin", "068", "admin", 0, None),
        ("alfi", "056", "user", 3000000, "K002"),
        ("novi", "111", "user", 1200000, "K004"),
        ("aldi", "222", "user", 500000, "K007"),
        ("budi", "123", "user", 2000000, None),
        ("eka01", "333", "user", 500000, None),
    ]
    dataPengguna.clear()
    for username, password, level, saldo, kamarSewa in akunAwal:
        dataPengguna[username] = {
            "password": hashPassword(password),
            "level": level,
            "saldo": saldo,
            "kamarSewa": kamarSewa,
        }

    daftarKamar.clear()
    daftarKamar.update({
        "K001": {"tipe": "Standar", "harga": 750000, "fasilitas": "Kipas angin, Kasur, KM luar", "status": "Kosong", "penyewa": None},
        "K002": {"tipe": "Standar", "harga": 950000, "fasilitas": "Kipas angin, Kasur, KM dalam", "status": "Terisi", "penyewa": "alfi"},
        "K003": {"tipe": "Standar", "harga": 850000, "fasilitas": "Kipas angin, Kasur, Lemari, KM luar", "status": "Kosong", "penyewa": None},
        "K004": {"tipe": "Deluxe", "harga": 1500000, "fasilitas": "AC, Kasur, KM dalam, WiFi, Meja belajar", "status": "Terisi", "penyewa": "novi"},
        "K005": {"tipe": "Deluxe", "harga": 1800000, "fasilitas": "AC, Kasur, KM dalam, WiFi, Lemari, Balkon", "status": "Kosong", "penyewa": None},
        "K006": {"tipe": "Deluxe", "harga": 1650000, "fasilitas": "AC, Kasur, KM dalam, WiFi, Lemari", "status": "Kosong", "penyewa": None},
        "K007": {"tipe": "VIP", "harga": 2500000, "fasilitas": "AC, Kasur, KM dalam, WiFi, Lemari, Balkon, Smart TV, Kulkas mini", "status": "Terisi", "penyewa": "aldi"},
        "K008": {"tipe": "VIP", "harga": 2800000, "fasilitas": "AC, Kasur king, KM dalam, WiFi, Lemari, Balkon, Smart TV, Kulkas mini, Dapur kecil", "status": "Kosong", "penyewa": None},
    })

    riwayatPemesanan.clear()
    riwayatPemesanan.extend([
        {"username": "alfi", "idKamar": "K002", "harga": 950000, "tanggal": "2026-08-01 10:30:00"},
        {"username": "novi", "idKamar": "K004", "harga": 1500000, "tanggal": "2026-08-15 14:05:00"},
        {"username": "budi", "idKamar": "K001", "harga": 750000, "tanggal": "2026-09-03 09:12:00"},
        {"username": "aldi", "idKamar": "K007", "harga": 2500000, "tanggal": "2026-10-05 16:40:00"},
        {"username": "eka01", "idKamar": "K003", "harga": 850000, "tanggal": "2026-10-20 11:20:00"},
    ])


def strukturValid(data):
    if not isinstance(data, dict):
        return False
    pengguna = data.get("dataPengguna")
    kamar = data.get("daftarKamar")
    riwayat = data.get("riwayatPemesanan")
    if not isinstance(pengguna, dict) or not pengguna:
        return False
    if not isinstance(kamar, dict) or not isinstance(riwayat, list):
        return False
    for akun in pengguna.values():
        if not isinstance(akun, dict) or not kunciAkun <= akun.keys():
            return False
        if not isinstance(akun["password"], str):
            return False
    for item in kamar.values():
        if not isinstance(item, dict) or not kunciKamar <= item.keys():
            return False
    for item in riwayat:
        if not isinstance(item, dict) or not kunciRiwayat <= item.keys():
            return False
    return True


def sinkronkanData():
    for akun in dataPengguna.values():
        akun["kamarSewa"] = None
    for idKamar, kamar in daftarKamar.items():
        penyewa = kamar["penyewa"]
        valid = (
            kamar["status"] == "Terisi"
            and penyewa in dataPengguna
            and dataPengguna[penyewa]["kamarSewa"] is None
        )
        if valid:
            dataPengguna[penyewa]["kamarSewa"] = idKamar
        else:
            kamar["status"] = "Kosong"
            kamar["penyewa"] = None


def pindahkanFileRusak():
    try:
        os.replace(namaFile, f"{namaFile}.rusak-{int(time.time())}")
    except OSError:
        return "gagalBaca"
    isiDataAwal()
    return "rusak"


def muatData():
    try:
        with open(namaFile, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        isiDataAwal()
        return "baru"
    except (json.JSONDecodeError, UnicodeDecodeError):
        return pindahkanFileRusak()
    except OSError:
        return "gagalBaca"

    if not strukturValid(data):
        return pindahkanFileRusak()

    dataPengguna.clear()
    dataPengguna.update(data["dataPengguna"])
    daftarKamar.clear()
    daftarKamar.update(data["daftarKamar"])
    riwayatPemesanan.clear()
    riwayatPemesanan.extend(data["riwayatPemesanan"])

    for akun in dataPengguna.values():
        if not sudahDihash(akun["password"]):
            akun["password"] = hashPassword(akun["password"])
    sinkronkanData()
    return "ok"


def simpanData():
    data = {
        "dataPengguna": dataPengguna,
        "daftarKamar": daftarKamar,
        "riwayatPemesanan": riwayatPemesanan,
    }
    sementara = namaFile + ".tmp"
    try:
        with open(sementara, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        os.replace(sementara, namaFile)
        return True
    except (OSError, TypeError, ValueError):
        pesanGagal("Waduh, data gagal disimpan! Cek ruang disk atau izin foldernya ya.")
        return False