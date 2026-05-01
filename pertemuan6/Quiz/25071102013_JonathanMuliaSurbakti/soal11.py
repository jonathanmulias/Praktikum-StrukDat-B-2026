def tambah_buku(nama, harga, stok):
    if harga <= 0:
        print("Harga tidak boleh kurang dari 0")
    elif stok <= 0:
        print("atok tidak boleh kurang dari 0")

    return "nama : ", nama, ", harga : ", harga, ", stok : ", stok

list_buku = []
for i in range(3):
    nama = input("Masukkan nama buku yang ingin ditambah : ")
    harga = int(input("Masukkan harga buku : "))
    stok = int(input("Masukkan stok buku : "))
    list_buku.append(tambah_buku(nama, harga, stok))
    print("\n")

print(list_buku)





