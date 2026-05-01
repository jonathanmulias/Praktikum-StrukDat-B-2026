# keuangan.py
def format_rupiah(jumlah):
    return f'Rp {jumlah:,.0f}'.replace(',', '.')

# Kode ini hanya jalan jika file ini dijalankan langsung
# Tidak akan jalan jika file ini di-import dari file lain

if __name__ == '__main__':
    print('Testing module keuangan...')
    print(format_rupiah(50000)) # Rp 50.000