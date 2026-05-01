"""
Tugas 2: Implementasi Menggunakan Singly LinkedList 

Buatlah struktur manual menggunakan Class.

1. Buat class Node dan class HistoryLinkedList.
2. Buat metode tambah_pencarian_linked(keyword) yang menambahkan node baru di posisi Head.

Catatan: Di LinkedList, Anda hanya perlu mengubah pointer next node baru ke head lama.
3. Buat metode tampilkan_history() untuk mencetak riwayat.
"""

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class HistoryLinkedList:
    def __init__(self):
        self.head = None

    def tambah_pencarian_linked(self, keyword):
        newNode = Node(keyword)
        newNode.next = self.head
        self.head = newNode

    def tampilkan_history(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

history = HistoryLinkedList()

data = input("Masukkan Pencaharian : ")
history.tambah_pencarian_linked(data)

print("\nPencaharian sebelumnya :")
history.tampilkan_history()