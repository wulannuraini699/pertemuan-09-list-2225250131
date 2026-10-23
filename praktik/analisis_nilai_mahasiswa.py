def rata_rata(data):
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    lulus = []
    for n in data:
        if n >= batas:
            lulus.append(n)
    return lulus

nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

banyak_data = len(nilai)
total_nilai = sum(nilai)
nilai_min = min(nilai)
nilai_max = max(nilai)
rata = rata_rata(nilai)

list_lulus = nilai_lulus(nilai, batas=60)
jumlah_lulus = len(list_lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

print("RINGKASAN HASIL NILAI MAHASISWA")
print(f"Seluruh Data Nilai    : {nilai}")
print(f"Banyak Data           : {banyak_data}")
print(f"Total Nilai           : {total_nilai}")
print(f"Rata-rata Nilai       : {rata:.2f}")
print(f"Nilai Minimum         : {nilai_min}")
print(f"Nilai Maksimum        : {nilai_max}")
print("-" * 39)
print(f"Batas Kelulusan       : 60")
print(f"Jumlah Mahasiswa Lulus: {jumlah_lulus}")
print(f"Jumlah Belum Lulus    : {jumlah_belum_lulus}")
print(f"List Nilai Lulus      : {list_lulus}")
