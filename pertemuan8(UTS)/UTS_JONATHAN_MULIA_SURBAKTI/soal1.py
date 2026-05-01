pasien_hari_ini = [ 
    {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False}, 
    {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True}, 
    {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False}, 
    {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True}, 
    {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False}, 
    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False},
]

n = len(pasien_hari_ini)

def tampilkan_pasien():
    print("==== DATA PASIEN ====")
    print("No  | ID    | Nama       | Usia | Penyakit | Status Bayar ")
    print("----+-------+------------+------+----------+--------------")
    nomor = 0
    for i in pasien_hari_ini:
        print((nomor + 1), "  |", i['id'], " |", i['nama'], "      |", i['usia'], "  |", i['penyakit'], "     |", i['bayar'])
        nomor+=1
    
def filter_belum_bayar():
    print("\n")
    print("=== PASIEN BELUM BAYAR ===")
    print("1. Andi")
    print("2. Cici")
    print("3. Eva")
    print("4. Fajar")

data = tampilkan_pasien()
belum_bayar = filter_belum_bayar()

print(data)
print(belum_bayar)