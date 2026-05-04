level_diskon = ( 
    (500000, 15),   # belanja >= 500.000 -> diskon 15% 
    (300000, 10),   # belanja >= 300.000 -> diskon 10% 
    (100000,  5),   # belanja >= 100.000 -> diskon  5% 
    (0,        0),  # default            
)

def hitung_diskon(total_belanja, level_diskon, index=0):
    if index >= len(level_diskon):
        return (0, 0, total_belanja)
    
    batas, persen = level_diskon[index]
    if total_belanja >= batas:
        nominal_diskon = total_belanja * persen / 100
        total_bayar = total_belanja - nominal_diskon
        return (persen, nominal_diskon, total_bayar)
    else:
        return hitung_diskon(total_belanja, level_diskon, index + 1)

nama = input("Masukkan Nama Pembeli: ")
total_belanja = int(input("Masukkan Total Belanja: "))

persen, nominal, total_bayar = hitung_diskon(total_belanja, level_diskon)

print("\nRincian Diskon")
print(f"Nama Pembeli    : {nama}")
print(f"Total Belanja   : Rp{total_belanja:,}")
print(f"Diskon          : {persen}%")
print(f"Nominal Diskon  : Rp{int(nominal):,}")
print(f"Total Bayar     : Rp{int(total_bayar):,}")

   