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
        new = Node(id_buku, judul)

        if self.root == None:
            self.root = new
            print(f"[INSERT] Berhasil memasukkan : ID {id_buku} - {judul}")
            return
        
        p = self.root
        q = self.root

        while q is not None:
            p = q

            if new.id < p.id:
                q = p.left
            elif new.id > p.id:
                q = p.right
            else:
                print("Data duplikat")
                return

        if new.id < p.id:
            p.left = new
        else:
            p.right = new
            
        print(f"[INSERT] Berhasil memasukkan : ID {id_buku} - {judul}")
        
    def search(self, id_buku):
        p = self.root

        while p is not None:
            if id_buku == p.id:
                return p
            elif id_buku < p.id:
                p = p.left
            else:
                p = p.right

        return None

    def inorder(self, node, no):
        if node:
            no = self.inorder(node.left, no)
            print(f"{no}. {node.id} - {node.judul}")
            no += 1
            no = self.inorder(node.right, no)
        return no

    def get_min(self):
        p = self.root
        while p.left is not None:
            p = p.left
        return p
    
    def get_max(self):
        p = self.root
        while p.right is not None:
            p = p.right
        return p
    
    def height(self, node):
        if node is None:
            return -1
        left = self.height(node.left)
        right = self.height(node.right)
        return max(left, right)

bst = BinarySearchTree()

print("SISTEM KATALOG PERPUSTAKAAN ILMU TERANG")
print("=======================================")

bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

print("\n[INFO] Koleksi Buku (In-Order Traversal):")
bst.inorder(bst.root, 1)

print("\n[SEARCH] Mencari ID 60...", end=" ")
hasil = bst.search(60)
if hasil:
    print(f"Ditemukan Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

print("[SEARCH] Mencari ID 100...", end = "")
hasil = bst.search(100)
if hasil:
    print(f"Ditemukan Judul: {hasil.judul}")
else:
    print(" Data tidak ditemukan")

print(f"\n[STATISTIK] ID Terkecil: {bst.get_min().id}")
print(f"[STATISTIK] ID Terbesar: {bst.get_max().id}")

print(f"[INFO] Tinggi (Height) Tree: {bst.height(bst.root)}")

print("=======================================")
print("Simulasi Selesai!")

            
            
