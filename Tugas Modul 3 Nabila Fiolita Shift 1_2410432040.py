print( "* *" *20 )
print("*              PERMAINAN TEBAK ANGKA BOM                   *")
print( "* *" *20 )
print("---------------PEMAIN 1-----------------")
n=int(input("Masukkan nilai n:"))
k=int(input("Angka BOM:"))
h="BOM"
for z in range (1,n+1) :
    if z%k==0 :
        print("BOM")
        z+=1
     
    else:
        print(z)

print("-----------------PEMAIN 2-----------------------")
a=int(input(f"Tebak angka dari 1 sampai {n}:"))
while a<n+1 :
    if a%k==0 :
        print(a,"adalah angka BOM, kemenangan Anda tertunda :(")
        a+=1
        break

    else :
        print(a,"bukan angka BOM,cie menang :)")
        break
if a > n :
        print(a," tidak ada dalam rentang pilihan, coba lagi yaa!")

print("TERIMAKASIH SUDAH BERMAIN!!")
print("  Kamu akan selalu merasa gagal bila tidak pernah mencoba~  ")
print( "* *" *20 )
