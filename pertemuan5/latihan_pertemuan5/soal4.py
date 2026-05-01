#Ubah jumlah buku menjadi 8.
transaksi = [
    {"produk": "Buku", "harga": 10000, "jumlah": 3},
    {"produk": "Pena", "harga": 5000, "jumlah": 10},
    {"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]

transaksi[0]["jumlah"] = 8
print(transaksi)

#Tambahkan 2 produk baru.
transaksi.append({"produk": "Pensil", "harga": 1000, "jumlah": 2})
transaksi.append({"produk": "Peraut", "harga": 2000, "jumlah": 4}) 

print(transaksi)           

#Hitung Total Pendapatan (Harga x Jumlah) untuk setiap transaksi menggunakan perulangan.
#Tampilkan ringkasan seperti ini:
#Produk: Buku | Total: 30000 Produk: Pena | Total: 50000 ... dan seterusnya.

for x in transaksi:
    total = (x["jumlah"] * x["harga"])

    print(f"{x["produk"]} | Total: {total}")