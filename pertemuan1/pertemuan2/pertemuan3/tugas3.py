class Person:
    def __init__(self, nama, jenis_kelamin, umur):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur

class Karyawan(Person):
    def __init__(self, nama, jenis_kelamin, umur, gaji):
         super().__init__(nama, jenis_kelamin, umur)
         self._gaji = gaji 
        
    def get_gaji(self):
        return self._gaji
    

class Rekening:
    def __init__(self, no_rekening, pin):
        self.no_rekening = no_rekening
        self.__pin = pin

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, pin_baru):
        self.__pin = pin_baru

person1 = Person("Erza", "Laki-laki", 18)
karyawan1 = Karyawan("Erza", "Laki-Laki", 18, 10000000)
rekening1 = Rekening(2660976445, 9999)

print(person1.nama, person1.jenis_kelamin, person1.umur)
print(karyawan1.nama, karyawan1.get_gaji())
print(rekening1.no_rekening, rekening1.get_pin())

rekening1.set_pin(3333)
print("Pin Baru", rekening1.get_pin()) 