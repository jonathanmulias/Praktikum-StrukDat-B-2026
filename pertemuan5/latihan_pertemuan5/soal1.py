#Ganti nilai 65 menjadi 75 menggunakan pencarian indeks.
nilai_tugas = [70, 85, 90, 65, 80]
nilai_tugas[3] = 75

print(nilai_tugas)

#Tambahkan nilai 95 ke dalam list, lalu urutkan list tersebut dari yang terbesar ke terkecil.
nilai_tugas.append(95)
nilai_tugas.sort(reverse=True)

print(nilai_tugas)

#Tampilkan jumlah total seluruh nilai dalam list tersebut.
jumlah = sum(nilai_tugas)

print(jumlah)

#Tampilkan pesan "Ada nilai sempurna" jika angka 100 ada di dalam list, jika tidak tampilkan "Tidak ada”.
if nilai_tugas == 100:
    print("Ada nilai sempurna")
else:
    print("Tidak ada")