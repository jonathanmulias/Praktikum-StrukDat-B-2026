"""
mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika",
"ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem
Informasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika",
"ipk": 3.75}

"""
print("---------------------------------------------------------------------------------------------------")
#1. Tampilkan nama mahasiswa yang memiliki IPK di atas 3.5.
print("SOAL 4.1")
mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika","ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "SistemInformasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika","ipk": 3.75}
}

for data in mahasiswa.values():
    if data["ipk"] > 3.5:
        print(data["nama"])

print("---------------------------------------------------------------------------------------------------")
#2. Hitung rata-rata IPK seluruh mahasiswa.
print("SOAL 4.2")
mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika","ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "SistemInformasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika","ipk": 3.75}
}

total_ipk = 0

for data in mahasiswa.values():
    total_ipk += data["ipk"]

rata_rata = total_ipk / len(mahasiswa)
print("Rata-rata IPK:", rata_rata)

print("---------------------------------------------------------------------------------------------------")
#3. Tambahkan satu data mahasiswa baru ke dalam dictionary tersebut.
print("SOAL 4.3")
mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika","ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "SistemInformasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika","ipk": 3.75}
}

mahasiswa["A004"] = {
    "nama": "Rina",
    "prodi": "Teknik Komputer",
    "ipk": 3.60
}
print(mahasiswa)

print("---------------------------------------------------------------------------------------------------")