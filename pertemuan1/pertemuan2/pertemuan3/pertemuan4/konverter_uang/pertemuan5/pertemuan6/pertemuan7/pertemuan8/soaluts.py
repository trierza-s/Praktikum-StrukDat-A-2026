# Soal 1 List dan Dictionary
pengunjung_hari_ini = [
{"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",
"kembali": False},
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",
"kembali": True},
{"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",
"kembali": False},
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",
"kembali": True},
{"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",
"kembali": False},
{"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",
"kembali": False},
]

def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID   | Nama   | Usia | Kategori | Status Kembali")
    print("---+------+--------+------+----------+---------------")

    for i, p in enumerate(pengunjung_hari_ini, start=1):
        status = "Sudah kembali" if p["kembali"] else "Belum kembali"
        print(f"{i:<2} | {p['id']} | {p['nama']:<6} | {p['usia']:<4} | {p['kategori']:<8} | {status}")

def filter_belum_kembali():
    belum_kembali = [p["nama"] for p in pengunjung_hari_ini if not p["kembali"]]
    belum_kembali.sort()

    print("\n===== PENGUNJUNG BELUM KEMBALI =====")
    for i, nama in enumerate(belum_kembali, start=1):
        print(f"{i}. {nama}")
    
    print(f"Total belum kembali: {len(belum_kembali)} pengunjung")

tampilkan_pengunjung()
filter_belum_kembali()


# Soal 2 Tuple dan Set
def info_perpustakaan():
    perpustakaan = (
        "Perpustakaan Kampus Terpadu",
        "Jl. Pendidikan No. 5, Pekanbaru",
        "0761-54321"
    )

    print("\nInfo Perpustakaan")
    print("Nama     :", perpustakaan[0])
    print("Alamat   :", perpustakaan[1])
    print("Telp     :", perpustakaan[2])

def rekap_kategori():
    buku_unik = {p["kategori"] for p in pengunjung_hari_ini}

    print("\nKategori Buku Unik:", buku_unik)
    print("Jumlah Kategori:", len(buku_unik))

    rekap = {}
    for p in pengunjung_hari_ini:
        buku = p["kategori"]
        rekap[buku] = rekap.get(buku, 0) + 1

    print("\nRekap per kategori:")
    for k, v in rekap.items():
        print(f"{k:<6}: {v} pengunjung")

    max_jumlah = max(rekap.values())
    terbanyak = [k for k, v in rekap.items() if v == max_jumlah]

    print(f"Kategori terbanyak: {', '.join(terbanyak)} ({max_jumlah} pengunjung)")

info_perpustakaan()
rekap_kategori()
print(" ")
 
# Soal 3 OOP
class Pengunjung:
    jumlah_pengunjung = 0

    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.jumlah_pengunjung += 1

    def get_id(self):
        return self.__id
    
    def get_nama(self):
        return self.__nama
    
    def get_kategori(self):
        return self.__kategori
    
    def tampilkan_info(self):
        print(f"ID      : {self.__id}")
        print(f"Nama    : {self.__nama}")
        print(f"Kategori: {self.__kategori}")

    @staticmethod
    def hitung_pengunjung():
        return Pengunjung.jumlah_pengunjung
    
class PengunjungPrioritas(Pengunjung):
    def __init__(self, id, nama, kategori, turunanPengunjung):
        super().__init__(id, nama, kategori)
        self.prioritas = turunanPengunjung

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Prioritas: {self.prioritas}")
        if self.prioritas == "Mendesak":
            print("** Layani Segera! **")

p1 = Pengunjung("M001", "Rina", "Fiksi")
p2 = PengunjungPrioritas("M007", "Gilang", "Referensi", "Mendesak")

p1.tampilkan_info()
print("\n")
p2.tampilkan_info()

print("\nTotal pengunjung terdaftar:", Pengunjung.hitung_pengunjung())

        