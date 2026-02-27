"""
1. Diberikan sebuah list angka:
angka = [10, 20, 30, 40, 50]

"""
print("---------------------------------------------------------------------------------------------------")
#1. Tambahkan angka 60 ke dalam list.
print("SOAL 1.1")
angka = [10, 20, 30, 40, 50]
angka = [10, 20, 30, 40, 50, 60]
print(angka)

print("---------------------------------------------------------------------------------------------------")
#2. Hapus angka 20 dari list.
print("SOAL 1.2")
angka = [10, 20, 30, 40, 50, 60]
angka.remove(20)
print(angka)

print("---------------------------------------------------------------------------------------------------")
#3. Tampilkan angka tertinggi dan terendah
print("SOAL 1.3")
angka = [10, 20, 30, 40, 50, 60]
print(max(angka), min(angka))

print("---------------------------------------------------------------------------------------------------")
#4. Hitung rata-rata angka setelah perubahan data
print("SOAL 1.4")
angka = [10, 20, 30, 40, 50, 60]
total = sum(angka) / len(angka)
print(total)

print("---------------------------------------------------------------------------------------------------")
#5. Tampilkan seluruh isi list setelah perubahan.
print("SOAL 1.5")
angka = [10, 20, 30, 40, 50, 60]
print(angka)

print("---------------------------------------------------------------------------------------------------")

