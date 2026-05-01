class Node:
  def __init__(self, data, keluhan, no_antrian):
    self.data = data
    self.keluhan = keluhan
    self.no_antrian = no_antrian
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.length = 0
    self.counter = 0

  def clear(self):
    self.front = None
    self.rear = None
    self.length = 0
    print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

  def enqueue(self, data, keluhan):
    self.counter += 1
    no_antrian = self.counter

    new_node = Node(data, keluhan, no_antrian)

    if self.rear is None:
      self.front = self.rear = new_node
    else:
      self.rear.next = new_node
      self.rear = new_node

    self.length += 1

    print(f"{data} terdaftar dengan keluhan : {keluhan} (No. Antrian : {no_antrian})")

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    temp = self.front
    self.front = temp.next
    self.length -= 1
    if self.front is None:
      self.rear = None
    print(f"Dokter memanggil: {temp.data} (keluhan: {temp.keluhan})\n")

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.front

  def isEmpty(self):
    return self.length == 0
  
  def cek_antrian(self):
    if self.isEmpty():
      print("Apakah antrian kosong? → YA, antrian kosong.\n")
    else:
      print("Apakah antrian kosong? → TIDAK, antrian tidak kosong.\n")

  def size(self):
    return self.length

  def printQueue(self):
    print("[ANTRIAN SAAT INI]")
    temp = self.front
    no = 1

    while temp:
        print(f"{no}. {temp.data.upper()} -> {temp.keluhan.lower()}")
        temp = temp.next
        no += 1

    print()

# Create a queue
print("==========================")
print(" SISTEM ANTRIAN POLI UMUM ")
print("     RS Sehat Bersama     ")
print("==========================\n")

myQueue = Queue()

myQueue.cek_antrian()

myQueue.enqueue('Budi', 'Demam Tinggi')
myQueue.enqueue('Anita', 'Batuk Pilek')
myQueue.enqueue('Citra', 'Sakit Kepala')

print("\nJumlah pasien menunggu : ", myQueue.size(), "orang")

pasien = myQueue.peek()

print("pasien berikutnya : ", pasien.data, "-", pasien.keluhan, "\n")

myQueue.dequeue()

myQueue.enqueue('Dodi', 'nyeri perut')

myQueue.printQueue()

myQueue.dequeue()

print("Jumlah pasien masih menunggu : ", myQueue.size(), "orang\n")

myQueue.clear()

myQueue.cek_antrian()

print("\n==========================")
print("     Simulasi Selesai!    ")
print("==========================\n")
