# Nama File : 05_filter_kelulusan.py
# Deskripsi : Menyaring dan menghitung nilai yang memenuhi batas kelulusan (>= 60).

# Input / Inisialisasi Data
nilai = [75, 55, 80, 60, 45, 90]
batas_lulus = 60
lulus = []

# Proses Filtering
for x in nilai:
    if x >= batas_lulus:
        lulus.append(x)

# Output
print(f"Nilai lulus  = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")