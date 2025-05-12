n = int(input("Masukkan Jumlah Mahasiswa Praktikum ADP:"))
nama = []
nilai = []
jumlah_akhir = 0

for i in range(n):
    b = input("Masukkan Nama: ")
    c = int(input("Masukkan Nilai Pretest: "))
    d = int(input("Masukkan Nilai Postest: "))
    e = int(input("Masukkan Nilai Makalah: "))
    
    total = 0.4 * c + 0.4 * d + 0.2 * e
    jumlah_akhir += total
    
    nama.append(b)
    nilai.append(total)

print("\n" + "_" * 35)
print(f"{'Nama Mahasiswa':20} | {'Nilai Akhir':12}")
print("_" * 35)
for i in range(n):
    print(f"{nama[i]:20} | {nilai[i]:12.2f}")

# Cari nilai tertinggi dan terendah
nilai_tertinggi = nilai[0]
nilai_terendah = nilai[0]
nama_tertinggi = nama[0]
nama_terendah = nama[0]

for i in range(n):
    if nilai[i] > nilai_tertinggi:
        nilai_tertinggi = nilai[i]
        nama_tertinggi = nama[i]
    elif nilai[i] < nilai_terendah:
        nilai_terendah = nilai[i]
        nama_terendah = nama[i]

print("_" * 35)
print(f"Rata-Rata Nilai Akhir: {(jumlah_akhir / n):.2f}")
print("_" * 35)
print(f"Nilai Tertinggi: {nilai_tertinggi:.2f}\nNama Mahasiswa: {nama_tertinggi}")
print(f"Nilai Terendah : {nilai_terendah:.2f}\nNama Mahasiswa: {nama_terendah}")
print("_" * 35)

# Tampilkan nama yang nilai di atas rata-rata
print("Nama Mahasiswa Di Atas Rata-Rata ")
print("_" * 35)
rata_rata = jumlah_akhir / n
for i in range(n):
    if nilai[i] > rata_rata:
        print(nama[i])
print("_" * 35)


