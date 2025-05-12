n=int(input("Masukkan Jumlah Mahasiswa Praktikum ADP:"))
a=[]
jumlah_akhir=0
for i in range(n):
    b=input("Masukkan Nama:")
    c=int(input("Masukkan Nilai Pretest:"))
    d=int(input("Masukkan Nilai Postest:"))
    e=int(input("Masukkan Nilai Makalah:"))
    nilai_akhirpretest=0.4*c
    nilai_akhirpostest=0.4*d
    nilai_akhirmakalah=0.2*e
    total=nilai_akhirpretest+nilai_akhirpostest+nilai_akhirmakalah
    jumlah_akhir+=total
    a.append((b,total))
print("\n"+ "_"*35) 
print(f"{'Nama Mahasiswa':20} {'|'} {'Nilai Akhir':12}")
print("_"*35)
for b , total in a:
    print(f"{b:20} {'|'} {total:12.2f}")
g=a[0]
h=a[0]
for j in range(len(a)):
    if a[j][1]>h[1]:
        h=a[j]
    elif a[j][1]<g[1]:
        g=a[j]
print("_"*35)
print(f"Rata-Rata Nilai Akhir:{(jumlah_akhir/n):.2f}")
print("_"*35)
print(f'Nilai Tertinggi:{h[1]:.2f}\nNama Mahasiswa :{h[0]}')
print(f'Nilai Terendah :{g[1]:.2f}\nNama Mahasiswa :{g[0]}')
print("_"*35)
l=jumlah_akhir/n
print("Nama Mahasiswa Di Atas Rata-Rata ")
print("_"*35)
for data in a:
    if data[1]>l:
        print(f"{data[0]}")
print("_"*35)

   


