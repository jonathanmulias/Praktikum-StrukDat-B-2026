# Gunakan perulangan untuk memproses setiap tuple tersebut. Jika nilai >= 75, 
# tampilkan: "Selamat [Nama], Anda Lulus!". Jika di bawah 75, 
# tampilkan: "Maaf [Nama], Anda harus remidi."

kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]
for data in kumpulan_nilai:
    if data[1] >= 75:
        print(f"Selamat {data[0]}, Anda Lulus!")
    if data[1] <= 75:
        print(f"Maaf {data[0]}, Anda harus remidi.")
