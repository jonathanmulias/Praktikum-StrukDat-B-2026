"""
2. Case: Sistem Antrean Pasien (Emergency Room)
   Skenario: Di sebuah rumah sakit, pasien datang dengan tingkat urgensi yang berbeda. Secara
   default, pasien baru akan mengantre di belakang. Namun, jika ada pasien "Darurat", mereka harus
   disisipkan di posisi tertentu (misalnya posisi ke-2) agar segera ditangani setelah pasien pertama
   yang sedang diperiksa.

   Data Awal (Antrean saat ini): ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

Tugas 1: Implementasi pada List Array

Gunakan list bawaan Python antrean_array.

1. Buat list antrean_array dengan data awal di atas.
2. Buat fungsi sisipkan_pasien_darurat_array(nama_pasien, posisi):

Gunakan metode .insert(posisi - 1, nama_pasien).
Analisis: Apa yang terjadi pada pasien di belakangnya saat pasien baru masuk di tengah?

3. Cetak antrean akhir.
"""
print("SELAMAT DATANG DI EMERGENCY ROOM")
print("jika ada pasien baru, maka akan mengantre di belakang")
print("jika ada pasien Darurat, maka harus disisipkan di posisi tertentu (misalnya posisi ke-2)")

nama_pasien = input("Masukkan nama pasien : ")
posisi = int(input("Masukkan posisi antrian : "))

posisi = posisi - 1

antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    antrean_array.insert(posisi, nama_pasien)

sisipkan_pasien_darurat_array(nama_pasien, posisi)

print("\nAntrean pasien sekarang:")
print(antrean_array)