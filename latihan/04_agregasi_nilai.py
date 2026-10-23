# Nama File : 04_agregasi_nilai.py
# Deskripsi : Menghitung statistik dasar (total, rata-rata, minimum, maksimum) dari list numerik.

# Input / Inisialisasi Data
nilai = [75, 80, 65, 90, 88]

# Proses Agregasi & Output
total = sum(nilai)
banyak = len(nilai)
rata_rata = total / banyak

print(f"Total    = {total}")
print(f"Rata-rata = {rata_rata:.2f}")
print(f"Minimum  = {min(nilai)}")
print(f"Maksimum = {max(nilai)}")