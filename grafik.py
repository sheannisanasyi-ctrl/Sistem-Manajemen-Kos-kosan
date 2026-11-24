import pandas as pd
import matplotlib.pyplot as plt

from data import riwayatPemesanan
from utils import pesanPeringatan, pesanGagal

namaBulan = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "Mei", 6: "Jun",
             7: "Jul", 8: "Agu", 9: "Sep", 10: "Okt", 11: "Nov", 12: "Des"}


def hitungPendapatanBulanan():
    total = {}
    for transaksi in riwayatPemesanan:
        try:
            bulan = pd.Period(transaksi["tanggal"][:7], freq="M")
            harga = int(transaksi["harga"])
        except (ValueError, KeyError, TypeError):
            continue  
        total[bulan] = total.get(bulan, 0) + harga

    if not total:
        return None

    rentang = pd.period_range(min(total), max(total), freq="M")
    label = [f"{namaBulan[b.month]} {b.year}" for b in rentang]
    nilai = [total.get(b, 0) / 1_000_000 for b in rentang]
    return pd.Series(nilai, index=label)


def tampilGrafik():
    pendapatan = hitungPendapatanBulanan()
    if pendapatan is None:
        pesanPeringatan("Belum ada data pemesanan buat dibikin grafik nih!")
        return

    try:
        plt.figure(figsize=(8, 4))
        batang = plt.bar(pendapatan.index, pendapatan.values, color="royalblue")
        plt.bar_label(batang, labels=[f"{v:g}" for v in pendapatan.values], padding=2)
        plt.title("Pendapatan per Bulan")
        plt.xlabel("Bulan")
        plt.ylabel("Pendapatan (juta Rupiah)")
        plt.grid(True, axis="y")
        plt.tight_layout()
        plt.show()
    except Exception as error:
        pesanGagal(f"Waduh, grafiknya gagal ditampilkan: {error}")
    finally:
        plt.close("all")