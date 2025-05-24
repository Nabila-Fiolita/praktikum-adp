print("Masukkan ukuran matriks A")
baris_A=int(input("Berapa baris matriks A:"))
kolom_A=int(input("Berapa kolom matriks A:"))
n=[]
for i in range(baris_A):
    baris=[]
    for j in range(kolom_A):
        elemen=int(input(f"Masukkan elemen matriks [{i+1}][{j+1}]:"))
        baris.append(elemen)
    n.append(baris)
print("Masukkan ukuran matriks B")
baris_B=int(input("Berapa baris matriks B:"))
kolom_B=int(input("Berapa kolom matriks B:"))
m=[]
for i in range(baris_B):
    baris=[]
    for j in range(kolom_B):
        elemen=int(input(f"Masukkan elemen matriks [{i+1}][{j+1}]:"))
        baris.append(elemen)
    m.append(baris)
print("Menu Kalkulator Matriks")
print("1.Penjumlahan Matriks")
print("2.Pengurangan Matriks")
print("3.Perkalian Matriks")
print("4.Determinan Matriks")
print("5.Invers Matriks")
print("6.Transpose Matriks")
print("7.Selesai")
while True:
    apa=int(input("Silahkan pilih operasi(1-7):"))
    if apa==1:
        if baris_A!=baris_B or kolom_A!=kolom_B:
             print("Ukuran matriks harus sama!")
        else:
            u=[]
            for i in range(baris_A):
                jumlah=[]
                for j in range(kolom_A):
                 hasil=n[i][j]+m[i][j]
                 jumlah.append(hasil)
                u.append(jumlah)
            print("Hasil penjumlahan yaitu")
            for jumlah in u:
                print(jumlah)
    elif apa==2:
        if baris_A!=baris_B or kolom_A!=kolom_B:
                print("Ukuran matriks harus sama!")
        else:
            a=[] 
            for i in range(baris_A):
                 jumlah=[]
                 for j in range(kolom_A):
                     hasil=n[i][j]-m[i][j]
                     jumlah.append(hasil)
                 a.append(jumlah)
            print("Hasil pengurangan yaitu")
            for jumlah in a:
                    print(jumlah)
    elif apa==3:
            if kolom_A!=baris_B:
                 print("Ukuran matriks harus sama!")
            else:
                b=[]
                for i in range(baris_A):
                    jumlah=[]
                    for j in range(kolom_B):
                        total=0
                        for k in range(kolom_A):
                            total+=n[i][k]*m[k][j]
                        jumlah.append(total)
                    b.append(jumlah)
                print("Hasil perkalian yaitu")
                for jumlah in b:
                        print(jumlah)
    elif apa==4 or apa==5:
            if baris_A!=kolom_A or baris_B!=kolom_B:
                print("Tidak bisa dihitung, bukan matriks persegi!")
            else:
                if apa==4:
                 if baris_A==1 and kolom_A==1:
                     detn=n[i][j]
                     print(f"Determinan matriks A yaitu {detn}")
                     detm=m[i][j]
                     print(f"Determinan matriks B yaitu {detm}")
                 elif baris_A==2 and kolom_A==2:
                         detn=(n[0][0]*n[1][1])-(n[0][1]*n[1][0])
                         print(f"Determinan matriks A yaitu {detn}")
                         detm=(m[0][0]*m[1][1])-(m[0][1]*m[1][0])
                         print(f"Determinan matriks B yaitu {detm}")
                 elif baris_A==3 and kolom_A==3:
                     detn=(((n[0][0]*n[1][1]*n[2][2])+(n[0][1]*n[1][2]*n[2][0])+(n[0][2]*n[1][0]*n[2][1]))
                           -((n[0][2]*n[1][1]*n[2][0])+(n[0][1]*n[1][0]*n[2][2])+(n[0][0]*n[1][2]*n[2][1])))
                     print(f"Determinan matriks A yaitu {detn}")
                     detm=(((m[0][0]*m[1][1]*m[2][2])+(m[0][1]*m[1][2]*m[2][0])+(m[0][2]*m[1][0]*m[2][1]))
                           -((m[0][2]*m[1][1]*m[2][0])+(m[0][1]*m[1][0]*n[2][2])+(m[0][0]*m[1][2]*m[2][1])))
                     print(f"Determinan matriks B yaitu {detm}")
                 elif  baris_A>=4 or kolom_A>=4 or baris_B>=4 or kolom_B>=4:
                         print("Program untuk menghitung determinan ini dibatasi maksimal sampai matriks 3x3")
                elif apa==5:
                     if baris_A==1 and kolom_A==1:
                         if n[i][j]!=0 and m[i][j]!=0:
                             invA=1/n[i][j]
                             print(f"Invers matriks A yaitu {invA:.2f}")
                             invB=1/m[i][j]
                             print(f"Invers matriks B yaitu {invB:.2f}")
                         else:
                             print("Invers tidak ada karena elemen matriks adalah 0")
                     elif baris_A == 2 and kolom_A == 2 or baris_B==2 and kolom_B==2:
                         detA = n[0][0]*n[1][1] - n[0][1]*n[1][0]
                         if detA != 0:
                             invA = [
                                 [n[1][1]/detA, -n[0][1]/detA],
                                 [-n[1][0]/detA, n[0][0]/detA]
                                 ]
                             print("Invers matriks A yaitu:")
                             for row in invA:
                              print(row)
                         else:
                                  print("Invers matriks A tidak ada karena determinannya 0!")
                         detB=m[0][0]*m[1][1]-m[0][1]*m[1][0]
                         if detB != 0:
                             invB=[
                                 [m[1][1]/detB, -m[0][1]/detB],
                                 [-m[1][0]/detB, m[0][0]/detB]
                             ]
                             print("Invers matriks B yaitu ")
                             for row in invB:
                                 print(row)
                         else:
                          print("Invers matriks B tidak ada karena determinannya 0!")      
                     elif baris_A==3 and kolom_A==3 or baris_B==3 and kolom_B==3:
                       detA=((n[0][0]*(n[1][1]*n[2][2])-n[1][2]*n[2][1])-n[0][1]*(n[1][0]*n[2][2]-n[1][2]*n[2][0])
                               +n[0][2]*(n[1][0]*n[2][1]-n[1][1]*n[2][0]))
                       if detA!=0:
                            for _ in range(3):
                                cofactor =[[0]*3]
                                cofactor[0][0] =  (n[1][1]*n[2][2] - n[1][2]*n[2][1])
                                cofactor[0][1] = -(n[1][0]*n[2][2] - n[1][2]*n[2][0])
                                cofactor[0][2] =  (n[1][0]*n[2][1] - n[1][1]*n[2][0])
                                cofactor[1][0] = -(n[0][1]*n[2][2] - n[0][2]*n[2][1])
                                cofactor[1][1] =  (n[0][0]*n[2][2] - n[0][2]*n[2][0])
                                cofactor[1][2] = -(n[0][0]*n[2][1] - n[0][1]*n[2][0])
                                cofactor[2][0] =  (n[0][1]*n[1][2] - n[0][2]*n[1][1])
                                cofactor[2][1] = -(n[0][0]*n[1][2] - n[0][2]*n[1][0])
                                cofactor[2][2] =  (n[0][0]*n[1][1] - n[0][1]*n[1][0])
                                for j in range(3):
                                    for i in range(3):
                                        adj=[cofactor[j][i]]
                                for j in range(3):
                                    for i in range(3):
                                        invA=[[adj[i][j]/detA]]      
                                for j in range(3):
                                    for i in range(3):
                                        print(f"{invA:.2f}")
                       else:
                             print("Invers tidak ada karena determinannya adalah 0")
                       detB=((m[0][0]*(m[1][1]*m[2][2])-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
                               +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
                       if detB!=0:
                            for _ in range(3):
                                cofactor =[[0]*3]
                                cofactor[0][0] =  (m[1][1]*m[2][2] - m[1][2]*m[2][1])
                                cofactor[0][1] = -(m[1][0]*m[2][2] - m[1][2]*m[2][0])
                                cofactor[0][2] =  (m[1][0]*m[2][1] - m[1][1]*m[2][0])
                                cofactor[1][0] = -(m[0][1]*m[2][2] - m[0][2]*m[2][1])
                                cofactor[1][1] =  (m[0][0]*m[2][2] - m[0][2]*m[2][0])
                                cofactor[1][2] = -(m[0][0]*m[2][1] - m[0][1]*m[2][0])
                                cofactor[2][0] =  (m[0][1]*m[1][2] - m[0][2]*m[1][1])
                                cofactor[2][1] = -(m[0][0]*m[1][2] - m[0][2]*m[1][0])
                                cofactor[2][2] =  (m[0][0]*m[1][1] - m[0][1]*m[1][0])
                                for j in range(3):
                                    for i in range(3):
                                        adj=[cofactor[j][i]]
                                for j in range(3):
                                    for i in range(3):
                                        invB=[[adj[i][j]/detB]]      
                                for j in range(3):
                                    for i in range(3):
                                        print(f"{invB:.2f}")
                       else:
                             print("Invers tidak ada karena determinannya adalah 0")
                     elif baris_A>=4 or kolom_A>=4 or baris_B>=4 or kolom_B>=4:
                         print("Program untuk menghitung invers  ini dibatasi maksimal sampai matriks 3x3")
    elif apa==6:
        print("Transpose matriks A")
        for i in range(kolom_A):
            for j in range(baris_A):
                print(f"{n[j][i]}", end=" ")
            print()
        print("Transpose matriks B")
        for i in range(kolom_B):
            for j in range(baris_B):
                print(f"{m[j][i]}", end=" ")  
            print()
    else:
        break     
