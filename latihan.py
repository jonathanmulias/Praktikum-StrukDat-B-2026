"CONTOH PROGRAM 2, MENGGUNAKAN INPUT"

print("Menu Martabak Djoeragan")
print("1. Martabak Cokelat    ")
print("2. Martabak Keju       ")

for i in range(3):
    nama = input("Masukkan nama anda: ")
    pesanan = int(input("Masukkan kode pesanan anda: "))
    jumlah = int(input("Masukkan jumlah pesanan anda: "))
    print("\n")

class Person:
  def __init__(self, nama, pesanan, jumlah, antrian):
    self.nama = nama
    self.pesanan = pesanan
    self.jumlah = jumlah
    self.antrian = antrian

  def ubah_pesanan(self, pesanan):
    self.pesanan = pesanan

  def ubah_jumlah(self, jumlah):
    self.jumlah = jumlah

p1 = Person(nama, pesanan, jumlah, 1)
p2 = Person(nama, pesanan, jumlah, 2)
p3 = Person(nama, pesanan, jumlah, 3)

p2.ubah_pesanan(1)
p1.ubah_jumlah(2)
p2.ubah_jumlah(1)
p3.ubah_jumlah(2)

print("nama", p1.nama, "pesanan", p1.pesanan, "jumlah", p1.jumlah, "antrian", p1.antrian)
print("nama", p2.nama, "pesanan", p2.pesanan, "jumlah", p2.jumlah, "antrian", p2.antrian)
print("nama", p3.nama, "pesanan", p3.pesanan, "jumlah", p3.jumlah, "antrian", p3.antrian)

