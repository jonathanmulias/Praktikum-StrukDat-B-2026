from kurs import kurs

def konverter(jumlah, mata_uang_pertama, mata_uang_kedua):
    return jumlah * kurs[mata_uang_pertama] / kurs[mata_uang_kedua]

