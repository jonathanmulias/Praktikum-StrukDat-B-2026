#Tampilkan nama mahasiswa yang hadir di kedua sesi (pagi DAN siang)
sesi_pagi = {"Andi", "Budi", "Cici"} 
sesi_siang = {"Budi", "Deni", "Eka"}

seluruh_sesi = sesi_pagi & sesi_siang
print(seluruh_sesi)

#Tampilkan total daftar nama unik yang hadir hari itu (semua mahasiswa dari kedua sesi tanpa duplikat).
sesi_pagi = {"Andi", "Budi", "Cici"} 
sesi_siang = {"Budi", "Deni", "Eka"}

total_daftar = sesi_pagi.intersection(sesi_siang)
print(total_daftar)

#Gabungkan kedua set tersebut menjadi satu set bernama sesi_hari_ini.
sesi_pagi = {"Andi", "Budi", "Cici"} 
sesi_siang = {"Budi", "Deni", "Eka"}

sesi_hari_ini = sesi_pagi.symmetric_difference(sesi_siang)
print(sesi_hari_ini)
