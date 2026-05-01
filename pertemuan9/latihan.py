"""
Bagian A — Double Linked List

Sistem daftar buku toko "Literasi"
Toko buku "Literasi" ingin mencatat daftar buku (judul & pengarang)
menggunakan Double Linked List agar bisa ditelusuri dari depan maupun belakang.

1. Buat class Node dengan atribut judul, pengarang, prev, dan next.
2. Buat fungsi insert_tail(), lalu tambahkan buku: Laskar Pelangi, Bumi Manusia, dan Sang Pemimpi.
3. Buat fungsi print_forward() dan print_backward(), lalu jalankan keduanya.
4. Buat fungsi delete_by_judul(), hapus buku "Bumi Manusia", lalu tampilkan list kembali.
"""

print("========================")
print("   Double Linked List   ")
print("========================\n")

class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, judul, pengarang):
        new_node = Node(judul, pengarang)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def print_forward(self):
        temp = self.head
        while temp:
            print(f"{temp.judul} - {temp.pengarang}")
            temp = temp.next
        print()

    def print_backward(self):
        temp = self.head

        if temp is None:
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(f"{temp.judul} - {temp.pengarang}")
            temp = temp.prev
        print()

    def delete_by_judul(self, judul):
        temp = self.head

        while temp:
            if temp.judul == judul:
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                return
            temp = temp.next

        print("Buku tidak ditemukan!")

dll = DoubleLinkedList()

#Tambah data buku
dll.insert_tail("Laskar Pelangi", "Andrea Hirata")
dll.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
dll.insert_tail("Sang Pemimpi", "Andrea Hirata")

#Menampilkan buku
print("Urutan buku dari depan : ")
dll.print_forward()

print("Urutan buku dari belakang :")
dll.print_backward()

#Menghapus buku
print("Hapus buku 'Bumi Manusia'\n")
dll.delete_by_judul("Bumi Manusia")

#Menampilkan kembali data buku
print("Setelah buku dihapus (depan) : ")
dll.print_forward()

print("Setelah buku dihapus (belakang) : ")
dll.print_backward()

"""
Bagian B — Circular Linked List

Sistem antrian kasir toko "Literasi"
Kasir toko menggunakan Circular Linked List untuk antrian pelanggan. Antrian
awal: Andi → Budi → Citra → Dina → (kembali ke Andi).

1. Buat class Node dengan atribut nama dan next. Buat fungsi insert_tail() dan tambahkan 4 pelanggan.
2. Buat fungsi print_antrian() untuk menampilkan satu putaran antrian.
3. Tambahkan pelanggan baru Edo di akhir antrian menggunakan insert_tail(), lalu tampilkan antrian.
4. Buat fungsi delete_head(), hapus Andi (sudah dilayani), lalu tampilkan antrian.
"""

print("========================")
print("  Circular Linked List  ")
print("========================\n")

class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, nama):
        new_node = Node(nama)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def print_antrian(self):
        if self.head is None:
            print("Antrian kosong")
            return

        temp = self.head
        while True:
            print(temp.nama, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("kembali ke awal")

    def delete_head(self):
        if self.head is None:
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next

cll = CircularLinkedList()

#Menambahkan 4 pelanggan awal
cll.insert_tail("Andi")
cll.insert_tail("Budi")
cll.insert_tail("Citra")
cll.insert_tail("Dina")

#Menampilkan antrian
print("Antrian awal:")
cll.print_antrian()

#Menambahkan Edo
print("\nMenambahkan Edo:")
cll.insert_tail("Edo")
cll.print_antrian()

#Menghapus Andi (head)
print("\nHapus Andi (sudah dilayani):")
cll.delete_head()
cll.print_antrian()



