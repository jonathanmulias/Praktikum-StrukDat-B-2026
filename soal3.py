"""
3. Diberikan dua set mata kuliah pilihan:
kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

"""
print("---------------------------------------------------------------------------------------------------")
#1. Tentukan mata kuliah yang diambil oleh kedua kelas.
print("SOAL 3.1")
kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

kelas_diambil = kelas_A.intersection(kelas_B)
print(kelas_diambil)

print("---------------------------------------------------------------------------------------------------")
#2. Tentukan mata kuliah yang hanya diambil kelas A.
print("SOAL 3.2")
kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

kelas_diambil = kelas_A
print(kelas_diambil)

print("---------------------------------------------------------------------------------------------------")
#3. Tentukan seluruh mata kuliah unik yang diambil oleh kelas A dan B.
print("SOAL 3.3")

kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

kelas_diambil = kelas_A.symmetric_difference(kelas_B)
print(kelas_diambil)

