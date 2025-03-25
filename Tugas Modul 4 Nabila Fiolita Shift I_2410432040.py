
while True:
     r=int(input("Masukkan jumlah baris kursi (minimal 4):"))
     c=int(input("Masukkan jumlah kolom kursi (minimal 4):"))
     a=r*c
     kursi=""
     if r < 4 or c < 4 :
                  print("Ukuran minimal bioskop adalah 4 x 4 ! Silahkan masukkan ulang !")
                  continue
     else:
              print("Layout Kursi Bioskop :")
              for j in range(1,a+1):
                         print(f"{j:1}",end="\t")
                         if j%r==0 :
                                
                                print("")
                         else:
                              continue
     break
while r>=4 and c>=4 :
        t=int(input("Masukkan nomor kursi yang ingin dipesan (atau 0 untuk selesai) :"))
        pilih="" 
        if t>a+1:
               print(f"Mohon maaf, kursi {t} tidak tersedia.\nSilahkan pilih kursi yang lain!")
        elif str(t) in kursi:
               print(f"Kursi {t} sudah  dipesan, pilih yang lain yaa!")
        elif t==0:
               print("Terimakasih sudah memesan!")
               break
        else:
               print(f"Kursi {t} berhasil dipesan !") 
               kursi+=f"{t}"
               print("Layout Kursi Bioskop :")
               k=0
               for i in range(1,a+1):
                     if str(i) in kursi:
                        print("X", end="\t")
                     else:
                        print(f"{i:<2}", end="\t")  
                     k+=1
                     if k % c==0 :
                       print("")
                                                       
                     else:
                           continue
     
            
  