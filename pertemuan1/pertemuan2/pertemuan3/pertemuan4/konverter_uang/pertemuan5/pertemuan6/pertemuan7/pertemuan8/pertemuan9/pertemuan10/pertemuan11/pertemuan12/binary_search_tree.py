class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    
    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)

        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.id < current.id:
            if current.left is None:
                current.left = new_node
                print(f"[INSERT] Berhasil memasukkan: ID {new_node.id} - {new_node.judul}")
            else:
                self._insert_recursive(current.left, new_node)
        elif new_node.id > current.id:
            if current.right is None:
                current.right = new_node
                print(f"[INSERT] Berhasil memasukkan: ID {new_node.id} - {new_node.judul}")
            else:
                self._insert_recursive(current.right, new_node)

    
    def search(self, id_buku):
        return self._search_recursive(self.root, id_buku)

    def _search_recursive(self, current, id_buku):
        if current is None:
            return None

        if id_buku == current.id:
            return current
        elif id_buku < current.id:
            return self._search_recursive(current.left, id_buku)
        else:
            return self._search_recursive(current.right, id_buku)

    
    def inorder(self):
        print("\n[INFO] Koleksi Buku (In-Order Traversal):")
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current):
        if current is not None:
            self._inorder_recursive(current.left)
            print(f"{current.id} - {current.judul}")
            self._inorder_recursive(current.right)

    
    def get_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    
    def get_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1  # biar sesuai contoh (root dihitung 0)
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1


# Program Utama
print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("=========================================")

tree = BinarySearchTree()


tree.insert(50, "Dasar Pemrograman")
tree.insert(30, "Struktur Data")
tree.insert(70, "Kecerdasan Buatan")
tree.insert(20, "Matematika Diskrit")
tree.insert(40, "Basis Data")
tree.insert(60, "Jaringan Komputer")
tree.insert(80, "Sistem Operasi")


tree.inorder()


print("\n[SEARCH] Mencari ID 60...")
result = tree.search(60)
if result:
    print(f"Ditemukan! Judul: {result.judul}")
else:
    print("Data tidak ditemukan.")

print("\n[SEARCH] Mencari ID 100...")
result = tree.search(100)
if result:
    print(f"Ditemukan! Judul: {result.judul}")
else:
    print("Data tidak ditemukan.")


min_buku = tree.get_min()
max_buku = tree.get_max()

print(f"\n[STATISTIK] ID Terkecil: {min_buku.id}")
print(f"[STATISTIK] ID Terbesar: {max_buku.id}")


print(f"\n[INFO] Tinggi (Height) Tree: {tree.height()}")

print("=========================================")
print("Simulasi Selesai!")