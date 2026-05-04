def pisahkan_plat(data):
    ganjil = []
    genap = []

    for plat in data:
        angka = ''.join(filter(str.isdigit, plat))
        angka_terakhir = int(angka[-1])

        if angka_terakhir % 2 == 0:
            genap.append(plat)
        else:
            ganjil.append(plat)

    return ganjil, genap

data = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

ganjil, genap = pisahkan_plat(data)

print("Plat Ganjil:", ganjil)
print("\nPlat Genap:", genap)

