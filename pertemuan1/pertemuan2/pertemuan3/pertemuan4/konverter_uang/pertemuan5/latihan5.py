# 1
stok_barang = [15, 40, 30, 10, 25]
x = stok_barang.index(10)
print(x)

stok_barang[3] = 50
print(stok_barang)

stok_barang.append(5)
print(stok_barang)

stok_barang.sort(reverse=True)
print(stok_barang)

stok_barang = sum(stok_barang)
print(stok_barang)
stok_barang = [15, 40, 30, 50, 25, 5]
print("Stok Aman" if (sum(stok_barang)/len(stok_barang)) > 20 else "Waspada")
print(" ")

# 2
data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for nama, poin in data_aktivitas:
    if poin > 80:
        print(f"{nama} mendapatkan predikat Gold")
    elif 50 <= poin <= 80:
        print(f"{nama} mendapatkan predikat Silver")
    else:
        print(f"{nama} mendapatkan predikat Bronze")
print(' ')

# 3
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

A = ukm_coding.difference(ukm_robotik)
ukm = ukm_coding.union(ukm_robotik)
print(ukm)
print(A)
print("Andi" in ukm_robotik)
print(" ")

# 4
gudang_pc = [
    {"item": "Monitor", "harga": 1500000, "stok": 5},
    {"item": "Keyboard", "harga": 400000, "stok": 12},
    {"item": "Mouse", "harga": 250000, "stok": 20}
]
for produk in gudang_pc:
    if produk["item"] == "Keyboard":
        produk["kategori"] = "Aksesoris"
gudang_pc.append({"item": "Headset", "harga": 350000, "stok": 8})
for produk in gudang_pc:
    total_aset = produk["harga"] * produk["stok"]
    print(f"Item: {produk['item']} | Total Aset: Rp {total_aset}")
