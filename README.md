# Pertemuan 09 List
Nama: Wulan Nur'aini
NIM: 2225250131
Kelas: 3E

## Tujuan
Memahami dan mengimplementasikan konsep struktur data List di Python, meliputi pembuatan, pengindeksan, pemotongan (slicing), manipulasi elemen, serta penerapan fungsi agregasi dan filter data untuk pengolahan nilai.

## Cara Menjalankan
python3 praktik/analisis_nilai_mahasiswa.py

## Struktur Fungsi
1. hitung_rata_rata(data)
Parameter: data (list angka/float/int)
Return Value: float (nilai rata-rata dari seluruh elemen list)
Deskripsi: Menghitung rata-rata nilai dari kumpulan data angka dalam list.
2. filter_lulus(data, batas_lulus)
Parameter: data (list angka/float/int), batas_lulus (float/int)
Return Value: list (daftar nilai yang lebih besar atau sama dengan batas_lulus)
Deskripsi: Menyaring dan mengembalikan list baru yang berisi nilai-nilai yang memenuhi kriteria kelulusan.
3. tampilkan_ringkasan(data, batas_lulus)
Parameter: data (list angka/float/int), batas_lulus (float/int)
Return Value: Tidak ada (None)
Deskripsi: Menampilkan ringkasan statistik analisis nilai mahasiswa secara terstruktur ke layar terminal.

## Hasil Pengujian

| No | Fungsi / Latihan | Input / Test Case | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | `01_buat_list.py` | `01_buat_list.py` | `[75, 80, 65, 90, 88]`, `Banyak data = 5` | `[75, 80, 65, 90, 88]`, `Banyak data = 5` | Berhasil |
| 2 | `02_indeks_slicing.py` | `02_indeks_slicing.py` | `75`, `70`, `[75, 80, 65]`, `[80, 65, 90]` | `75`, `70`, `[75, 80, 65]`, `[80, 65, 90]` | Berhasil |
| 3 | `03_manipulasi_list.py` | `03_manipulasi_list.py` | `[75, 70, 82, 90]` | `[75, 70, 82, 90]` | Berhasil |
| 4 | `04_agregasi_nilai.py` | `04_agregasi_nilai.py` | `Total = 398`, `Rata-rata = 79.60`, `Minimum = 65`, `Maksimum = 90` | `Total = 398`, `Rata-rata = 79.60`, `Minimum = 65`, `Maksimum = 90` | Berhasil |
| 5 | `05_filter_kelulusan.py` | `05_filter_kelulusan.py` | `Nilai lulus = [75, 80, 60, 90]`, `Jumlah lulus = 4` | `Nilai lulus = [75, 80, 60, 90]`, `Jumlah lulus = 4` | Berhasil |
| 6 | `06_fungsi_statistik.py` | `06_fungsi_statistik.py` | `Rata-rata = 79.60` | `Rata-rata = 79.60` | Berhasil |
| 7 | `analisis_nilai_mahasiswa.py` | `analisis_nilai_mahasiswa.py` | `Total = 695`, `Rata-rata = 69.50`, `Lulus = 7`, `Belum Lulus = 3` | `Total = 695`, `Rata-rata = 69.50`, `Lulus = 7`, `Belum Lulus = 3` | Berhasil |

## Refleksi
Penerapan struktur data List dan fungsi agregasi membuat pengolahan kumpulan data angka menjadi jauh lebih efisien dan terstruktur:
1. Efisiensi Penyimpanan Data: Seluruh nilai mahasiswa dapat disimpan dalam satu variabel List tanpa perlu membuat banyak variabel terpisah.
2. Kemudahan Manipulasi Data: Penggunaan slicing, looping, dan list comprehension mempermudah penyaringan data (seperti menentukan batas kelulusan) secara ringkas.
3. Pemanfaatan Fungsi Bawaan: Fungsi bawaan Python seperti sum(), len(), min(), dan max() mempercepat perhitungan statistik dasar tanpa harus menuliskan perulangan manual dari awal.
