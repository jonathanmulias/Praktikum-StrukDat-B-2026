"CONTOH PROGRAM 1, TIDAK MENGGUNAKAN INPUT"

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

p1 = Person("Jonathan", 2, 1, 1)
p2 = Person("Riva", 2, 1, 2)
p3 = Person("Gama", 1, 2, 3)

p1.ubah_jumlah(2)
p2.ubah_pesanan(1)

print("nama", p1.nama, "pesanan", p1.pesanan, "jumlah", p1.jumlah, "antrian", p1.antrian)
print("nama", p2.nama, "pesanan", p2.pesanan, "jumlah", p2.jumlah, "antrian", p2.antrian)
print("nama", p3.nama, "pesanan", p3.pesanan, "jumlah", p3.jumlah, "antrian", p3.antrian)



