from data import daftarKamar, riwayatPemesanan, tipeKamar
from utils import formatRupiah, buatTabel, pesanPeringatan


def tampilDashboard():
    totalKamar = len(daftarKamar)
    kamarTerisi = 0
    for kamar in daftarKamar.values():
        if kamar["status"] == "Terisi":
            kamarTerisi += 1
    kamarKosong = totalKamar - kamarTerisi
    okupansi = round(kamarTerisi / totalKamar * 100, 1) if totalKamar > 0 else 0

    totalPendapatan = 0
    for transaksi in riwayatPemesanan:
        totalPendapatan += transaksi["harga"]

    tabelStatistik = buatTabel("RINGKASAN STATISTIK SISTEM", ["Keterangan", "Data"])
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
    tabel = buatTabel("REKAPITULASI PER TIPE KAMAR", ["Tipe Kamar", "Kosong", "Terisi"])
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
        pesanPeringatan("Belum ada riwayat pemesanan nih!")
        return

    tabel = buatTabel("TRANSAKSI PEMESANAN TERBARU (MAKS. 5)", ["User", "ID Kamar", "Harga", "Tanggal"])
    for transaksi in reversed(riwayatPemesanan[-5:]):
        tabel.add_row([transaksi["username"], transaksi["idKamar"],
                       formatRupiah(transaksi["harga"]), transaksi["tanggal"]])
    print(tabel)