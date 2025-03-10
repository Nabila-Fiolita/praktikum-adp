#tampilan 1
nama=input("Nama =")
umur=int(input("Umur ="))
jenis_kelamin=input("Jenis Kelamin =")
#tampilan 2
print("Kode Maskapai :")
print("a. 3012")
print("b. 4015")
print("c. 4050")
kode_maskapai=input("Pilih Kode Maskapai =")
if kode_maskapai == "3012" :
    print("Tujuan Maskapai Padang-Jakarta")
elif kode_maskapai == "4015" :
    print("Tujuan Maskapai Padang-Batam")
elif kode_maskapai == "4050" :
    print("Tujuan Maskapai Padang-Bandung")
#tampilan 3
print( "____________________________________________________________________________")
print("|                          Menu Jenis Maskapai                              |")
print("|___________________________________________________________________________|")
print("|Kode Maskapai |   Kelas Ekonomi  |   Kelas Bisnis    |    Kelas First Class|")
print("|______________|__________________|___________________|_____________________|")
print("|   3012       |    Rp.800.000    |     Rp.850.000    |         Rp.900.000  |")
print("|   4015       |    Rp.500.000    |     Rp.550.000    |         Rp.700.000  |")
print("|   4050       |    Rp.700.000    |     Rp.750.000    |         Rp.850.000  |")                                         
print("|______________|__________________|___________________|_____________________|")
print("PEMBELIAN TIKET LEBIH DARI 3 AKAN MENDAPATKAN DISKON SEBESAR 20%")
jenis_maskapai=input("Masukkan jenis maskapai :")
if kode_maskapai == "3012"and jenis_maskapai == "Kelas Ekonomi" :
     b =800000
elif kode_maskapai  == "3012" and jenis_maskapai== "Kelas Bisnis":
     b=850000
elif kode_maskapai    == "3012" and jenis_maskapai== "Kelas First Class" :
    b=900000
elif kode_maskapai   == "4015" and jenis_maskapai == "Kelas Ekonomi" :
    b=500000
elif kode_maskapai  == "4015" and jenis_maskapai== "Kelas Bisnis" :
    b=550000
elif kode_maskapai  == "4015" and jenis_maskapai=="Kelas First Class" :
    b=700000
elif kode_maskapai   == "4050" and jenis_maskapai=="Kelas Ekonomi" :
    b=700000
elif kode_maskapai   == "4050" and jenis_maskapai=="Kelas Bisnis" :
    b=750000
elif kode_maskapai  == "4015" and jenis_maskapai=="Kelas First Class":
     b=850000 
n=int(input("Jumlah Kursi yang Dipesan :"))
if n > 3 :
    a=0.2
else :
    a=0
harga_potongan_diskon= n * b * a
total_harga=(n * b ) - harga_potongan_diskon 
 #tampilan 4
print("                 Struk Pemesanan      ")
print("1.Nama               :", nama)
print("2.Umur               :", umur)
print("3.Jenis Kelamin      :", jenis_kelamin)
print("-------------------------------------------")
print("4.Kode Maskapai        :", kode_maskapai  )
print("5.Jenis Maskapai       :", jenis_maskapai)
print("6.Jumlah Tiket         :", n)
print("7.Total Harga          :", total_harga)
print(       "SEMOGA PERJALANAN ANDA MENYENANGKAN !")
