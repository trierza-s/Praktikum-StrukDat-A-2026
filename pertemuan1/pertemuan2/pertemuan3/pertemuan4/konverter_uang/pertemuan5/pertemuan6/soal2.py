katalog = [ 
    {'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
    {'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
] 


def cari_buku(katalog, keyword):
    hasil = []
    for buku in katalog:
        if keyword.lower() in buku['nama'].lower():
            hasil.append(buku)
    if not hasil:
        print("Buku tidak ditemukan.")
    return hasil

keyword = input("Masukkan Keyword Yang Ingin Dicari: ")
hasil_pencarian = cari_buku(katalog, keyword)

if hasil_pencarian:
    print("\nHasil pencarian:")
    for buku in hasil_pencarian:
        print(f"Judul : {buku['nama']}")
        print(f"Harga : Rp{buku['harga']:,}")
        print(f"Stok  : {buku['stok']} buah")
