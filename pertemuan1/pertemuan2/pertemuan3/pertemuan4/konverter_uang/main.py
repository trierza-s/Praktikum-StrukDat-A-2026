from kurs import kurs
from konverter import konversi
from tabulate import tabulate

print("=== KONVERTER MATA UANG ===")

tabel = [[k, f"{v:,}".replace(",", ".")] for k, v in kurs.items()]
print(tabulate(tabel, headers=["Kode", "Kurs"], tablefmt="grid"))

dari = input("\nDari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke  (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

hasil = konversi(jumlah, dari, ke)

jumlah_format = f"{jumlah:,.0f}".replace(",",".")
if dari == "IDR":
    print(f"\nRp {jumlah_format} = {hasil:.2f} {ke}")
elif ke == "IDR":
    hasil_format = f"{hasil:,.0f}".replace(",",".")
    print(f"\n{jumlah} {dari} = Rp {hasil_format}")
else:
    print(f"\n{jumlah} {dari} = {hasil:.2f} {ke}")