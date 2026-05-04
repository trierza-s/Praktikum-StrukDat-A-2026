mahasiswa = {
"M001": {"nama": "Rina", "prodi": "Informatika", "ipk":
3.60},
"M002": {"nama": "Doni", "prodi": "Sistem Informasi",
"ipk": 3.25},
"M003": {"nama": "Lina", "prodi": "Informatika", "ipk":
3.80}
}

for nim, data in mahasiswa.items():
    if data["prodi"] == "Informatika" and data ["ipk"] >= 3.50:
        print(data["nama"])

total_ipk = sum([data["ipk"] for data in mahasiswa.values()])
rata_ipk = total_ipk / len(mahasiswa)
print(f"Rata-rata IPK: {rata_ipk:.2f}")

mahasiswa["M004"] = {"nama": "Erza", "prodi": "Teknik Informatika", "ipk": 4.00}

for nim, data in mahasiswa.items():
    print(nim, ":", data)

