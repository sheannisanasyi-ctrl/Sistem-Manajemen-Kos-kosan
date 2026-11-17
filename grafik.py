# import pandas as pd
# import matplotlib.pyplot as plt
# from data import riwayatPemesanan
# from utils import tekanEnter

# namaBulan = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "Mei", "06": "Jun",
#              "07": "Jul", "08": "Agu", "09": "Sep", "10": "Okt", "11": "Nov", "12": "Des"}


# def tampilGrafik():
#     if not riwayatPemesanan:
#         print("Belum ada data pemesanan untuk dibuat grafik.")
#         tekanEnter()
#         return

#     pendapatanBulan = {}
#     for riwayat in riwayatPemesanan:
#         bulan = riwayat["tanggal"][:7]
#         if bulan in pendapatanBulan:
#             pendapatanBulan[bulan] += riwayat["harga"]
#         else:
#             pendapatanBulan[bulan] = riwayat["harga"]

#     label = []
#     nilai = []
#     for bulan in sorted(pendapatanBulan.keys()):
#         label.append(namaBulan[bulan[5:7]] + " " + bulan[:4])
#         nilai.append(pendapatanBulan[bulan] / 1000000)

#     pendapatan = pd.Series(nilai, index=label)

#     plt.figure(figsize=(8, 4))
#     plt.plot(pendapatan.index, pendapatan.values, marker="o", color="blue")
#     plt.title("Pendapatan per Bulan")
#     plt.xlabel("Bulan")
#     plt.ylabel("Pendapatan (juta Rp)")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()