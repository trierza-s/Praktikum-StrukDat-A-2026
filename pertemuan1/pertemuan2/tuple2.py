dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
print(dosen[1])
print(dosen[2])

for x in dosen:
    print(x)

y = list(dosen)
y[-1] = 14
dosen = tuple(y)
print(dosen)
#Poin 3/ angka 12(sks) bakal berubah menjadi 14(sks) 
#Poin 4/ lebih rumit (menurut saya)