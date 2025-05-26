def input_data(n):
    a = []
    for i in range(n):
        b = input(f"Masukkan Nama Mahasiswa Ke-{i+1}: ")
        c = int(input("Masukkan NIM: "))
        d = float(input("Masukkan Nilai UTS: "))
        e = float(input("Masukkan Nilai UAS: "))
        f = float(input("Masukkan Nilai Tugas: "))
        a.append([b, c, d, e, f])
    return a

def rata_uts(a):
    total = 0
    for i in range(len(a)):
        total += a[i][2]
    return total / len(a)

def rata_uas(a):
    total = 0
    for i in range(len(a)):
        total += a[i][3]
    return total / len(a)

def rata_tugas(a):
    total = 0
    for i in range(len(a)):
        total += a[i][4]
    return total / len(a)

def nilai_akhirmhs(a):
    for mhs in a:
        nilaiakhirmhs = 0.35 * mhs[2] + 0.35 * mhs[3] + 0.30 * mhs[4]
        mhs.append(nilaiakhirmhs)

def rata_akhir(a):
    total = 0
    for mhs in a:
        total += mhs[5]
    return total / len(a)

def terter(a):
    hasil = []
    while a:
        maks = a[0]
        for mhs in a:
            if mhs[5] > maks[5]:
                maks = mhs
        hasil.append(maks)
        a.remove(maks)
    for i in hasil:
        a.append(i)

def peringkat(a):
    for i in range(len(a)):
        a[i].append(i + 1)

def tabel(a, rata1, rata2, rata3, rataakhir):
    print("\n{:<15} {:<10} {:<10} {:<10} {:<12} {:<12} {:<9}".format(
        "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Peringkat"))
    print("-" * 85)
    for mhs in a:
        print("{:<15} {:<10} {:<10.2f} {:<10.2f} {:<12.2f} {:<12.2f} {:<9}".format(
            mhs[0], mhs[1], mhs[2], mhs[3], mhs[4], mhs[5], mhs[6]))
    print("-" * 85)
    print("{:<15} {:<10} {:<10.2f} {:<10.2f} {:<12.2f} {:<12.2f}".format(
        "Rata-rata", "", rata1, rata2, rata3, rataakhir))

# Main Program
n = int(input("Masukkan jumlah mahasiswa: "))
a = input_data(n)
rata1 = rata_uts(a)
rata2 = rata_uas(a)
rata3 = rata_tugas(a)
nilai_akhirmhs(a)
rataakhir = rata_akhir(a)
terter(a)
peringkat(a)
tabel(a, rata1, rata2, rata3, rataakhir)

