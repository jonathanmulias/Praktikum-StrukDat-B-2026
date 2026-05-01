from konverter import konverter
from kurs import kurs
from tabulate import tabulate

print("=== KONVERTER MATA UANG ===")

data = [
    [kode, f"{nilai:,.0f}".replace(",", ".")]
    for kode, nilai in kurs.items()
    if kode != "IDR"
]

print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))

while True:
    mata_uang_pertama = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
    if mata_uang_pertama in kurs:
        break
    print("Mata uang tidak ditemukan\n")

while True:
    mata_uang_kedua = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
    if mata_uang_kedua in kurs:
        break
    print("Mata uang tidak ditemukan\n")

while True:
    try:
        jumlah = int(input("Jumlah: "))
        break
    except ValueError:
        print("Input harus berupa angka!")

hasil = konverter(jumlah, mata_uang_pertama, mata_uang_kedua)

if mata_uang_pertama in kurs:
    if mata_uang_pertama == "IDR":
        jumlah_format = f"Rp {jumlah:,.0f}".replace(",", ".")
    else:
        jumlah_format = f"{jumlah:,.2f} {mata_uang_pertama}"

if mata_uang_kedua == "IDR":
    hasil_format = f"Rp {hasil:,.0f}".replace(",", ".")
elif mata_uang_kedua == "JPY": 
    hasil_format = f"{hasil:,.0f} JPY"
else:
    hasil_format = f"{hasil:,.2f} {mata_uang_kedua}"

print(f"\n{jumlah_format} = {hasil_format}")

