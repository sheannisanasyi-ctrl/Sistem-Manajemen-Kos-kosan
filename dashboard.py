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
    
    print(f" Total Kamar       : {totalKamar}")
    print(f" Kamar Terisi      : {kamarTerisi}")
    print(f" Kamar Kosong      : {kamarKosong}")
    print(f" Tingkat Okupansi  : {okupansi}%")
    print(f" Total Pendapatan  : {formatRupiah(totalPendapatan)}")
    print(f" Total User Terdaftar: {totalUser}")
    print("=" * 44)
    print()
    
    rekapPerTipe()
    print()
    
    pemesananTerbaru()


def rekapPerTipe():
    print("[-] Rekapitulasi per Tipe Kamar:")
    tabel = PrettyTable(["Tipe Kamar", "Kosong", "Terisi"])
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
    print("[-] 5 Transaksi Pemesanan Terbaru:")
    if not riwayatPemesanan:
        print("Belum ada riwayat pemesanan, nih!")
        return

    tabel = PrettyTable(["User", "ID Kamar", "Harga", "Tanggal"])
    tabel.align = "c"
    tabel.hrules = ALL
    
    jumlah = 0
    for i in range(len(riwayatPemesanan) - 1, -1, -1):
        r = riwayatPemesanan[i]
        id_kamar = r.get("idKamar") or r.get("kamar", "-")
        tabel.add_row([r["username"], id_kamar, formatRupiah(r["harga"]), r["tanggal"]])
        jumlah += 1
        if jumlah == 5:
            break
            
    print(tabel)