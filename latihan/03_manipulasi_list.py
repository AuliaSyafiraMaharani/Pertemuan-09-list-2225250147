# Nama File : 03_manipulasi_list.py
# Deskripsi : Melakukan manipulasi list seperti mengubah, menambah, menyisipkan, dan menghapus elemen.

# Inisialisasi Data
nilai = [75, 80, 65]
print("Data awal            :", nilai)

# Manipulasi Elemen
nilai[1] = 82        # Mengubah elemen indeks 1 menjadi 82
nilai.append(90)     # Menambahkan 90 di akhir list
nilai.insert(1, 70)  # Menyisipkan 70 pada indeks 1
nilai.remove(65)     # Menghapus elemen ber-nilai 65

# Output Hasil Akhir
print("Data setelah manipulasi:", nilai)