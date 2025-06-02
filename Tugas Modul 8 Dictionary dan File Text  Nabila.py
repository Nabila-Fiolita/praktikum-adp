buku=[
      ["780-2-12-908789-1","Dictionary","Harum",56,240000,270000],
      ["780-3-12-956798-2","Mengatur Produktivitas","Fio",44,300000,340000],
      ["780-2-01-789659-11","SMART","Ais",37,40000,450000],
      ["780-1-31-783259-21","Atika?","Nazollafi",2,90000,100000],
      ["780-4-22-102154-81","Zombie Negeri Selatan","Elsa Deviinia",5,345000,400000],
      ["780-7-51-367284-10","Yuk Merajut!","Maxx Lion",2,56000,60000],
      ["780-4-21-367404-10","Aku Cukup","Fawwaz I",1,120000,130000],
      ["780-1-23-321332-14","Geometri Analitik","Asriadi",1,70000,75000],
      ["780-11-3-309362-34","Matematika Diskrit","Gede Surwaken",10,80000,85000],
      ["780-6-12-352134-71","Rumah Masa Depan 2","Joy Life",46,89000,90000]
      ]
with open('inventaris_buku.txt','w') as file:
    for ISBN,judul_buku,penulis,stok,harga_beli,harga_jual in buku:
      file.write(f"{ISBN},{judul_buku},{penulis},{stok},{harga_beli},{harga_jual}\n")

inventaris = []
with open('inventaris_buku.txt', 'r') as file:
    for line in file:
        data = line.split(",")
        buku1 = {
            "ISBN": data[0],
            "Judul": data[1],
            "Penulis": data[2],
            "Stok": int(data[3]),  # Pastikan tidak ada karakter aneh dalam data
            "Harga Beli": int(data[4]),
            "Harga Jual": int(data[5])
        }
        inventaris.append(buku1)

# Menulis laporan inventaris dengan potensi keuntungan
with open('laporan_inventaris.txt', 'w') as file:
    file.write(f"{'ISBN':<20}{'Judul Buku':<30}{'Penulis':<20}{'Stok':<10}{'Harga Beli':<15}{'Harga Jual':<15}{'Potensi Keuntungan':<20}\n")
    file.write("="*130 + "\n") 

    for buku1 in inventaris:
        potensi_keuntungan = (buku1["Harga Jual"] - buku1["Harga Beli"]) * buku1["Stok"]
        file.write(f"{buku1['ISBN']:<20}{buku1['Judul']:<30}{buku1['Penulis']:<20}{buku1['Stok']:<10}{buku1['Harga Beli']:<15}{buku1['Harga Jual']:<15}{potensi_keuntungan:<20}\n")

#Analisis Inventaris
tertinggi = inventaris[0] 
terendah= inventaris[0]

for buku1 in inventaris:
    potensi_keuntungan = (buku1["Harga Jual"] - buku1["Harga Beli"]) * buku1["Stok"]
    if potensi_keuntungan > (tertinggi["Harga Jual"] - tertinggi["Harga Beli"]) * tertinggi["Stok"]:
        tertinggi = buku1  
    elif potensi_keuntungan < (terendah["Harga Jual"] - terendah["Harga Beli"]) * terendah["Stok"]:
        terendah = buku1 
print(f"Buku dengan potensi keuntungan terbesar: {tertinggi['Judul']} oleh {tertinggi['Penulis']}, Potensi Keuntungan: {(tertinggi['Harga Jual'] - tertinggi['Harga Beli']) * tertinggi['Stok']}")
print(f"Buku dengan potensi keuntungan terendah: {terendah['Judul']} oleh {terendah['Penulis']}, Potensi Keuntungan: {(terendah['Harga Jual'] - terendah['Harga Beli']) * terendah['Stok']}")
total=0
for data in buku:
    total+=(data[3]*data[4])
print(f"Total nilai inventaris yaitu {total}")
restock_buku = []  
for data in buku:
    if data[3] < 5: 
        restock_buku.append(data[1])
print("Buku yang harus di re-stock yaitu")
for judul_buku in restock_buku:
    print(judul_buku)
