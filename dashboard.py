from prettytable import PrettyTable, ALL
from data import dataPengguna, daftarKamar, riwayatPemesanan, tipeKamar
from utils import formatRupiah


def tampilDashboard():
    totalKamar = len(daftarKamar)
    kamarTerisi = 0
    for kamar in daftarKamar.values():
        if kamar["status"] == "Terisi":
            kamarTerisi += 1
    kamarKosong = totalKamar - kamarTerisi
    okupansi = round(kamarTerisi / totalKamar * 100, 1) if totalKamar > 0 else 0

    totalPendapatan = 0
    for riwayat in riwayatPemesanan:
        totalPendapatan += riwayat["harga"]

    totalUser = 0
    for akun in dataPengguna.values():
        if akun["level"] == "user":
            totalUser += 1

    daftarPenyewa = set()
    for riwayat in riwayatPemesanan:
        daftarPenyewa.add(riwayat["username"])
    penyewaUnik = len(daftarPenyewa)

    print("=" * 40)
    print("          DASHBOARD ADMIN")
    print("=" * 40)
    print(f"Total kamar       : {totalKamar}")
    print(f"Kamar terisi      : {kamarTerisi}")
    print(f"Kamar kosong      : {kamarKosong}")
    print(f"Okupansi          : {okupansi}%")
    print(f"Total pendapatan  : {formatRupiah(totalPendapatan)}")
    print(f"Total user        : {totalUser}")
    print(f"Penyewa unik      : {penyewaUnik}")
    print()
    rekapPerTipe()
    print()
    pemesananTerbaru()


def rekapPerTipe():
    print("Rekap per Tipe Kamar")
    tabel = PrettyTable(["Tipe", "Kosong", "Terisi"])
    tabel.hrules = ALL
    for tipe in tipeKamar:
        kosong = 0
        terisi = 0
        for kamar in daftarKamar.values():
            if kamar["tipe"] != tipe:
                continue
            if kamar["status"] == "Kosong":
                kosong += 1
            else:
                terisi += 1
        tabel.add_row([tipe, kosong, terisi])
    print(tabel)


def pemesananTerbaru():
    print("Pemesanan Terbaru")
    if not riwayatPemesanan:
        print("Belum ada pemesanan.")
        return

    tabel = PrettyTable(["User", "Kamar", "Harga", "Tanggal"])
    jumlah = 0
    for i in range(len(riwayatPemesanan) - 1, -1, -1):
        r = riwayatPemesanan[i]
        tabel.add_row([r["username"], r["idKamar"], formatRupiah(r["harga"]), r["tanggal"]])
        jumlah += 1
        if jumlah == 5:
            break
    print(tabel)