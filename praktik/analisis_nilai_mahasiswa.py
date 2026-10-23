# Nama File : analisis_nilai_mahasiswa.py
# Deskripsi : Program analisis data nilai mahasiswa menggunakan fungsi, agregasi, dan filtering kelulusan.

def rata_rata(data):
    """Menghitung rata-rata dari list numerik. Mengembalikan 0 jika list kosong."""
    if len(data) == 0:
        return 0.0
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    """Mengembalikan list baru yang berisi nilai-nilai yang memenuhi batas kelulusan."""
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil

def main():
    # 1. Inisialisasi Data (Minimal 10 Nilai)
    nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
    batas_kelulusan = 60

    # 2. Pengolahan Data
    banyak_data = len(nilai)
    total_nilai = sum(nilai)
    rerata = rata_rata(nilai)
    nilai_min = min(nilai) if nilai else 0
    nilai_max = max(nilai) if nilai else 0

    # Filtering Kelulusan
    daftar_lulus = nilai_lulus(nilai, batas=batas_kelulusan)
    jumlah_lulus = len(daftar_lulus)
    jumlah_tidak_lulus = banyak_data - jumlah_lulus

    # 3. Output Ringkasan Statistik
    print("==========================================")
    print("      ANALISIS NILAI MAHASISWA            ")
    print("==========================================")
    print(f"Data Nilai        : {nilai}")
    print(f"Banyak Data       : {banyak_data}")
    print(f"Total Nilai       : {total_nilai}")
    print(f"Rata-rata Nilai   : {rerata:.2f}")
    print(f"Nilai Minimum     : {nilai_min}")
    print(f"Nilai Maksimum    : {nilai_max}")
    print("------------------------------------------")
    print(f"Batas Kelulusan   : {batas_kelulusan}")
    print(f"Daftar Nilai Lulus: {daftar_lulus}")
    print(f"Jumlah Lulus      : {jumlah_lulus}")
    print(f"Jumlah Belum Lulus: {jumlah_tidak_lulus}")
    print("==========================================")

if __name__ == "__main__":
    main()