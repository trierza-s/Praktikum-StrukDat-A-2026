# Bagian 1
class StackList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    

# Bagian 2
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None
    
    def push(self, url):
        new_node = Node(url)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        
        popped_url = self.top.url
        self.top = self.top.next
        self.count -= 1
        return popped_url
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.url
    
    def size(self):
        return self.count
    

stack = StackList()
stack = StackLinkedList()

while True:
    print("\nMenu:")
    print("1. Kunjungi URL")
    print("2. Kembali ke URL sebelumnya")
    print("3. Lihat URL saat ini")
    print("4. Jumlah URL dalam riwayat")
    print("5. Keluar")  

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        url = input("Masukkan URL yang ingin dikunjungi: ")
        stack.push(url)
        print(f"URL '{url}' telah ditambahkan ke riwayat.")
    
    elif pilihan == '2':
        print("Kembali ke URL sebelumnya:", stack.pop())

    
    elif pilihan == '3':
        print("URL saat ini:", stack.peek())

    elif pilihan == '4':
        print("Jumlah URL dalam riwayat:", stack.size())

    elif pilihan == '5':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")