katalog = [ 
    {'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
    {'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
]

riwayat_transaksi = set()

def proses_transaksi(katalog, nama_buku, jumlah_beli):
    for buku in katalog:
        if buku['nama'].lower() == nama_buku.lower():
            if buku['stok'] >= jumlah_beli:
                buku['stok'] -= jumlah_beli
                total = buku['harga'] * jumlah_beli
                print(f"Transaksi berhasil! Total bayar: Rp{total:,}")
                riwayat_transaksi.add(buku['nama'])
            else:
                print(f"Stok tidak mencukupi. Stok tersedia: {buku['stok']}")
            return
    print("Error: Buku tidak ditemukan di katalog.")

proses_transaksi(katalog, "Belajar Python", 2)
proses_transaksi(katalog, "Struktur Data", 1)
proses_transaksi(katalog, "Algoritma Dasar", 9)  

print("\nRiwayat buku yang pernah dibeli:")
for judul in riwayat_transaksi:
    print("-", judul)
