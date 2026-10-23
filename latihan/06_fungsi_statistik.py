# Nama File : 06_fungsi_statistik.py
# Deskripsi : Membuat fungsi untuk menghitung rata-rata dengan penanganan list kosong.

def rata_rata(data):
    """Menhitung rata-rata dari list numerik. Mengembalikan 0 jika list kosong."""
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

# Pengujian Fungsi
nilai = [75, 80, 65, 90, 88]
print(f"Rata-rata data       = {rata_rata(nilai):.2f}")

# Pengujian List Kosong
list_kosong = []
print(f"Rata-rata list kosong = {rata_rata(list_kosong):.2f}")