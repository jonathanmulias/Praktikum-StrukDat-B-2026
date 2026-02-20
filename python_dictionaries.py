#PYTHON DICTIONARIES
#|| PYTHON DICTIONARIES ||

print("-------------------------------------------------------------------------------------------------")

print("PYTHON DICTIONARIES")

Biodata = {
  "Nama": "Jonathan",
  "Hobi": "Menonton Film",
  "Tahun": 2007
}
print(Biodata)

#Outputnya :
#{'Nama': 'Jonathan', 'Hobi': 'Menonton Film', 'Tahun': 2007}

print("-------------------------------------------------------------------------------------------------")

Biodata = {
  "Nama": "Jonathan",
  "Hobi": "Menonton Film",
  "Tahun": 2007
}
print(Biodata["Nama"])

#Outputnya :
#Jonathan

print("-------------------------------------------------------------------------------------------------")

Biodata = {
  "Nama": "Jonathan",
  "Hobi": "Menonton Film",
  "Tahun": 2007,
  "Umur": 18
}
print(Biodata)

#Outputnya :
#{'Nama': 'Jonathan', 'Hobi': 'Menonton Film', 'Tahun': 2007, 'Umur': 18}

print("-------------------------------------------------------------------------------------------------")

Biodata = {
  "Nama": "Jonathan",
  "Hobi": "Menonton Film",
  "Tahun": 2007,
  "Umur": 18
}
print(len(Biodata))

#Outputnya :
#4

print("-------------------------------------------------------------------------------------------------")

Biodata = {
  "Nama": "Jonathan",
  "Mahasiswa": True,
  "Tahun": 2007,
  "Warna": ["Hijau", "Kuning", "Biru"]
}

print(Biodata)

#Outputnya :
#{'Nama': 'Jonathan', 'Mahasiswa': True, 'Tahun': 2007, 'colors': ['Hijau', 'Kuning', 'Biru']}

print("-------------------------------------------------------------------------------------------------")

Biodata = {
  "Nama": "Jonathan",
  "Hobi": "Menonton Film",
  "Tahun": 2007,
}
print(type(Biodata))

#Outputnya :
#<class 'dict'>

print("-------------------------------------------------------------------------------------------------")

Biodata = dict(nama = "Jonathan", umur = 18, kewarganegaraan = "Indonesia")
print(Biodata) 

#Outputnya :
#{'nama': 'Jonathan', 'umur': 18, 'kewarganegaraan': 'Indonesia'}

print("-------------------------------------------------------------------------------------------------")