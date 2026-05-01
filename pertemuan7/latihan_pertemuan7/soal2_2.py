"""
Tugas 2: Implementasi pada Singly LinkedList

Gunakan class Node dan AntreanLinkedList.

1. Implementasikan fungsi insert_at_position(head, nama_pasien, posisi) seperti kode yang 
   kamu punya sebelumnya (menggunakan logika position - 2).
2. Tugas Tambahan: Tambahkan validasi sederhana. Jika posisi yang dimasukkan lebih besar
   dari jumlah pasien yang ada, maka pasien tersebut otomatis diletakkan di paling akhir
   (Append).
"""

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class AntreanLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, nama_pasien, posisi):
        newNode = Node(nama_pasien)

        if self.head is None or posisi == 1:
            newNode.next = self.head
            self.head = newNode
            return
        
        current = self.head
        count = 1

        while current.next is not None and count < posisi - 1:
            current = current.next
            count += 1

        newNode.next = current.next
        current.next = newNode

    def tampilkan_antrean(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
antrean = AntreanLinkedList()

antrean.insert_at_position("Pasien A (Stabil)", 1)
antrean.insert_at_position("Pasien B (Stabil)", 2)
antrean.insert_at_position("Pasien C (Stabil)", 3)

print("SELAMAT DATANG DI EMERGENCY ROOM")
print("jika ada pasien baru, maka akan mengantre di belakang")
print("jika ada pasien Darurat, maka harus disisipkan di posisi tertentu (misalnya posisi ke-2)")

nama_pasien = input("Masukkan nama pasien : ")
posisi = int(input("Masukkan posisi antrian : "))
antrean.insert_at_position(nama_pasien, posisi)

print("\nAntrean pasien sekarang:")
antrean.tampilkan_antrean()