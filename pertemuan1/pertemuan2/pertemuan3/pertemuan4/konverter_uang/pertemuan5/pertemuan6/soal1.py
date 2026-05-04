def tambah_buku(nama, harga, stok):
    if harga <= 0:
        print("ERROR, Harga harus diatas 0!")
        return None
    
    if stok < 0:
        print("ERROR")
        return None
    
    buku = {
        "nama": nama,
        "harga": harga,
        "stok": stok,
        "status": "Valid"
    }

    return buku

list = []

for i in range(3):
    print(f"\n Input Buku Ke-{i+1}")
    nama = str(input("Nama: "))
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))

    data = tambah_buku(nama, harga, stok)

    if data:
        list.append(data)


print("\nDaftar Buku:")
for g in list:
    print(g)