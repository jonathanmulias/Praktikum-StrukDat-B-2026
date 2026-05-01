"""
1. Case: Sistem Riwayat Pencarian (Search History)
   Skenario: Anda sedang membuat fitur "Riwayat Pencarian" untuk sebuah browser. Setiap kali
   pengguna mencari sesuatu, kata kunci tersebut akan ditambahkan ke daftar riwayat. Pengguna bisa
   melihat riwayat dari yang paling baru hingga yang paling lama.
   Data Awal: ["google.com", "python.org"]

Tugas 1: Implementasi Menggunakan List (Array) Python Gunakan tipe data list bawaan Python.
1. Buatlah sebuah list bernama history_array.
2. Buat fungsi tambah_pencarian_array(keyword) yang menambahkan kata kunci baru ke posisi paling depan 
   (indeks 0).

Catatan: Di dalam Array, saat memasukkan data di depan, semua elemen di belakangnya harus bergeser.

3. Cetak isi history_array.
"""

pencarian = input("Masukkan keyword yang ingin anda cari :")

history_array = ["google.com", "python.org"]

def tambah_pencarian_array(keyword):
    history_array.insert(0, keyword)

tambah_pencarian_array(pencarian)

print("\nHasil pencarian sekarang")
print(history_array)