from prettytable import PrettyTable, ALL
from data import daftarKamar, riwayatPemesanan, tipeKamar
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

    tabelStatistik = PrettyTable()
    tabelStatistik.title = "RINGKASAN STATISTIK SISTEM"
    tabelStatistik.field_names = ["Keterangan", "Data"]
    tabelStatistik.align = "c"
    tabelStatistik.hrules = ALL

    tabelStatistik.add_row(["Total Kamar", totalKamar])
    tabelStatistik.add_row(["Kamar Terisi", kamarTerisi])
    tabelStatistik.add_row(["Kamar Kosong", kamarKosong])
    tabelStatistik.add_row(["Tingkat Okupansi", f"{okupansi}%"])
    tabelStatistik.add_row(["Total Pendapatan", formatRupiah(totalPendapatan)])

    print(tabelStatistik)
    print()
    rekapPerTipe()
    print()
    pemesananTerbaru()


def rekapPerTipe():
    tabel = PrettyTable()
    tabel.title = "REKAPITULASI PER TIPE KAMAR"
    tabel.field_names = ["Tipe Kamar", "Kosong", "Terisi"]
    tabel.align = "c"
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
    if not riwayatPemesanan:
        print("Belum ada riwayat pemesanan.")
        return

    tabel = PrettyTable()
    tabel.title = "5 TRANSAKSI PEMESANAN TERBARU"
    tabel.field_names = ["User", "ID Kamar", "Harga", "Tanggal"]
    tabel.align = "c"
    tabel.hrules = ALL

    jumlah = 0
    for i in range(len(riwayatPemesanan) - 1, -1, -1):
        r = riwayatPemesanan[i]
        tabel.add_row([r["username"], r["idKamar"], formatRupiah(r["harga"]), r["tanggal"]])
        jumlah += 1
        if jumlah == 5:
            break

    print(tabel)