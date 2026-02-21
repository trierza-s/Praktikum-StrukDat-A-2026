from kurs import kurs

def konversi(jumlah, dari, ke):
    # kalau dari idr 
    if dari == "IDR":
        jumlah_idr = jumlah 
    else:
        jumlah_idr = jumlah * kurs[dari]
    # kalau ke idr
    if ke == "IDR":
        return jumlah_idr
    else:
        return jumlah_idr / kurs[ke]