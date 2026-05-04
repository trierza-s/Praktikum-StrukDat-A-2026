class Node:
    def __init__(self, nama, keluhan):
           self.nama = nama
           self.keluhan = keluhan
           self.next = None

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self.head is None
    
    def size(self):
        return self._size
    
    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail  = new_node
        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (Antrian ke-{self._size})")
        
    def dequeue(self):
        if self.is_empty():
            return "Antrian kosong"
        
        removed = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        
        self._size -= 1
        print(f"[PANGGIL] {removed.nama} dengan keluhan: {removed.keluhan}")
        return removed
    
    def peek(self):
        if self.is_empty():
            print("Antrian kosong")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.head.nama.upper()} dengan keluhan: {self.head.keluhan}")

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik telah dibersihkan. Antrian kosong.")

    def display(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        
        print("[ANTRIAN SAAT INI]")
        current = self.head
        no = 1
        while current:
            print(f"{no}. {current.nama.upper():<10} -> {current.keluhan}")
            current = current.next
            no += 1

q = QueueLinkedList()

print("=================================================")
print(" SISTEM ANTRIAN POLI UMUM")
print("=================================================")

# 1
print("[CEK] Apakah antrian kosong? ->", "YA" if q.is_empty() else "TIDAK")

# 2-4
q.enqueue("Budi", "demam tinggi")   
q.enqueue("Ani", "batuk pilek")  
q.enqueue("Citra", "sakit kepala")

# 5
print(f"[INFO] Jumlah pasien menunggu: {q.size()} orang")

# 6
q.peek()

# 7
q.dequeue()

# 8
q.enqueue("Dodi", "nyeri perut")

# 9
q.display()

# 10
q.dequeue()

# 11
print(f"[INFO] Jumlah pasien masih menunggu: {q.size()} orang")

# 12
q.clear()

# 13
print("[CEK] Apakah antrian kosong? ->", "YA" if q.is_empty() else "TIDAK")

print("=================================================")
print(" SIMULASI SELESAI")
print("=================================================")