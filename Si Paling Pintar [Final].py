import os
import time
from termcolor import colored, cprint
import random

def clear():
    os.system('cls')
# Tampilan Awal
clear()
print(" "*80 + colored("|| ||", "magenta"))
print(" "*77 + colored(" \( ^.^ )/", "magenta"))
print(" "*75 + colored("SI PALING PINTAR", "magenta"))
print("")
time.sleep(1)

# Animasi Loading
for i in range(10):
    clear()
    print(" " * 80 + "Loading" + "." * ((i % 3) + 1))
    time.sleep(0.2)

clear()
print()
time.sleep(0.5)
print(" " * 70 + "YUK BERSAMA KITA " + colored("JADI PINTAR ! >.<", "magenta", attrs=["bold"]))
time.sleep(1)
print()
print(" "*80 + colored("|| ||", "magenta"))
print(" "*77 + colored(" \( ^.^ )/", "black"))
print(" "*78 + colored("with Ovi", "magenta"))
time.sleep(1)
print(" "*75 + colored("Teman Belajarmu", "magenta"))
time.sleep(2)
clear()
print(" "*80 + colored("🐰Ketentuan Kuis🐰","magenta"))
print(" "*50 + colored(">Kombinasi topik dan level yang sama hanya bisa dikerjakan sekali", "light_magenta"))
print(" "*50 + colored(">Setiap soal harus dijawab dalam waktu 60 detik", "light_magenta"))
print(" "*50 + colored(">Jika pemain menjawab setelah 60 detik, skor tidak akan berpengaruh", "light_magenta"))
print(" "*50 + colored(">Jika jawaban pemain benar, skor ditambah 1", "light_magenta"))
print(" "*50 + colored(">Jika jawaban pemain salah, skor dikurangi 1", "light_magenta"))
print(" "*50 + colored(">Pemain dapat melihat 'Si Paling Pintar' berdasarkan skor kuis", "light_magenta"))
print(" "*50 + colored(">Tujuan kuis murni untuk menambah wawasan, bukan ajang membanding-bandingkan","light_magenta"))
level = ["Easy", "Medium", "Hard"]

def awal():
    pilih = ["Sains", "Teka-Teki Logika", "Sejarah", "Matematika"]
    print(" "*80 + colored('MENU KUIS', 'magenta', 'on_light_magenta', attrs=['bold']))
    for i in pilih:
        cprint(i, 'magenta', attrs=['bold'])

def tambah_skor(nama, skor_baru):
    data ={}
    if os.path.exists('Si Paling Pintar.txt'):
        with open('Si Paling Pintar.txt', 'r') as f:
            for line in f:
                if ',' in line:
                    nama_file, nilai = line.strip().split(',')
                    data[nama_file] = int(nilai)
                    
    if nama in data:
        data[nama] += skor_baru
    else:
        data[nama] = skor_baru
    with open('Si Paling Pintar.txt', 'w') as f:
        for nama_file, nilai in data.items():
            f.write(f"{nama_file},{nilai}\n")

def sudah_kerjakan(nama, topik, level):
    if not os.path.exists('data_kuis.txt'):
        return False
    with open('data_kuis.txt', 'r') as file:
        for baris in file:
            bagian = [b.strip().lower() for b in baris.strip().split(',')]
            if len(bagian) == 3:
                nama_file, topik_file, level_file = bagian
                if nama_file == nama.lower() and topik_file == topik.lower() and level_file == level.lower():
                    return True
    return False

def simpan_data(nama, topik, level):
    with open('data_kuis.txt', 'a') as file:
        file.write(f"{nama},{topik},{level}\n")

def tanya(bio):
    print()
    pilih = ["Sains", "Teka-Teki Logika", "Sejarah", "Matematika"]
    n = input("Mau Kuis Apa?: ")
    if n not in pilih:
        print("Pilihan tidak tersedia.")
        return 0

    print(" "*80 + colored('LEVEL', 'magenta', 'on_light_magenta', attrs=['bold']))
    for i in level:
        cprint(i, 'magenta', attrs=['bold'])
    print()
    b = input("Mau Level Apa?: ")
    if sudah_kerjakan(bio, n, b):
        print(f"Kamu sudah pernah mengerjakan kuis {n} level {b}. Coba variasi lain yaa.")
        return 0
    clear()
    k = []
    if n == 'Sains' and b == 'Easy':
        k = [
            ["Seluruh benua di dunia telah bergerak selama miliaran tahun dan masih akan terus bergerak", "Benar", "Salah", "Benar"],
            ["AB Negatif ialah jenis darah yang paling langka", "Benar", "Salah", "Benar"],
            ["Besi termasuk benda yang bersifat isolator", "Benar", "Salah", "Salah"],
            ["Minyak bumi termasuk sumber daya alam terbarukan", "Benar", "Salah", "Salah"],
            ["Fungsi utama mitokondria dalam sel adalah menyimpan informasi genetik", "Benar", "Salah", "Salah"]
        ]
    elif n == 'Sains' and b == 'Medium':
        k = [
            ["Apa nama proses di mana batuan diubah menjadi bentuk baru akibat tekanan dan suhu tinggi?",
             "Pelapukan", "Erosi", "Metamorfisme", "Sedimentasi", "Metamorfisme"],
            ["Apa nama senyawa kimia dengan rumus NaCl?", "Air", "Asam sulfat", "Garam dapur", "Amonia", "Garam dapur"],
            ["Apa nama proses di mana cairan berubah menjadi gas pada suhu di bawah titik didihnya?",
             "Kondensasi", "Evaporasi", "Pembekuan", "Sublimasi", "Evaporasi"],
            ["Apa nama planet terbesar dalam tata surya?", "Saturnus", "Jupiter", "Neptunus", "Bumi", "Jupiter"],
            ["Organisme berikut yang tidak dapat berkembang biak di luar tubuh sel hidup yaitu",
             "Bakteri", "Protozoa", "Cendawan", "Virus", "Virus"]
        ]
    elif n == 'Sains' and b == 'Hard':
        k = [
            ["Hipoklorit (NaOCl) merupakan senyawa yang banyak digunakan untuk?", "Pembersih", "Pemutih", "Pewangi", "Pelembut", "Pembersih"],
            ["Nama lain dari calyx adalah", "Mahkota bunga", "Bakal buah", "Putik", "Kelopak bunga", "Kelopak bunga"],
            ["Apa nama proses di mana inti atom berat terpecah menjadi inti yang lebih ringan, melepaskan energi?",
             "Fusi nuklir", "Ionisasi", "Radioaktivitas", "Fisi nuklir", "Fisi nuklir"],
            ["Apa nama hukum yang menyatakan bahwa tekanan fluida berkurang saat kecepatannya meningkat?",
             "Hukum Bernoulli", "Hukum Pascal", "Hukum Archimedes", "Hukum Boyle", "Hukum Bernoulli"],
            ["Jika sebuah benda bermassa 5 kg bergerak dengan kecepatan 10 m/s, berapa energi kinetiknya?",
             "250 J", "100 J", "450 J", "257 J", "250 J"]
        ]
    elif n == 'Matematika' and b == 'Easy':
        k = [
            ["Hasil dari -16 + (-15 : 3) adalah -21", "Benar", "Salah", "Benar"],
            ["5 x (-3) + 2! = -13", "Benar", "Salah", "Benar"],
            ["Tia berangkat sekolah pukul 9.30 dan pulang pukul 12.45, maka ia di sekolah selama 3 jam 48 menit", "Benar", "Salah", "Salah"],
            ["Nilai modus dari data 2,2,5,3,3,2 adalah 2", "Benar", "Salah", "Benar"],
            ["5 m= 5000 cm", "Benar", "Salah", "Salah"]
        ]
    elif n == 'Matematika' and b == 'Medium':
        k = [
            ["Hitung nilai x jika 3x+7=22", "5", "10", "-3", "7", "5"],
            ["Selesaikan persamaan 5-2y=11", "-3", "2", "6", "0", "-3"],
            ["Suku ke 10 dari barisan aritmetika: 4,7,10,13,.. adalah", "35", "31", "48", "29", "31"],
            ["Sebuah taman berbentuk lingkaran memiliki keliling 62,8 meter. Hitunglah jari-jari taman tersebut!", "10 m", "12 m", "18 m", "14 m", "10 m"],
            ["Sebuah bilangan jika dikalikan 4, kemudian dikurangi 5, hasilnya sama dengan bilangan itu sendiri ditambah 19. Berapa bilangan itu?", "10", "8", "7", "3", "8"]
        ]
    elif n=='Matematika' and b=='Hard':
        k= [
           ["Banyak cara enam orang siswa akan duduk pada tiga meja bundar, dimana setiap meja akan diduduki oleh minimal satu siswa(Jawab angka saja)","225"],
           ["Suatu dadu ditos 6 kali.Banyak cara memperoleh jumlah mata yang muncul 28 dengan tepat satu dadu muncul angka 6 adalah(Jawab angka saja)","210"],
           ["Banyaknya bilangan 8 digit yang setiap digitnya adalah 1 atau 2 tetapi tidak memuat 3 digit 1 berurutan adalah","149"],
           ["a+2b=1...(1) b+2c=2...(2) dan b bukan 0.Jika a+nb+2018c=2019, maka berapa n?","1011"],
           ["Jika selisih akar-akar persamaan sama dengan 5, maka jumlah akar-akar persamaan adalah","11 atau -11"]
            ]
    elif n=='Teka-Teki Logika' and b=='Easy':
        k=[
          ["Jika hari ini bukan Senin, maka besok adalah Selasa",
          "Benar","Salah","Salah"],
          ["Jika ada orang yang selalu jujur, maka setiap orang selalu berkata benar","Benar","Salah","Salah"],
          ["Jika tidak semua kucing berwarna hitam, maka ada kucing yang berwarna selain hitam.","Benar","Salah","Benar"],
          ["Jika A lebih besar dari B dan B lebih besar dari C, maka A lebih kecil dari C.","Benar","Salah","Salah"],
          ["Jika seorang dokter memberi kamu tiga pil dan meminta untuk meminumnya setiap setengah jam, kamu akan menghabiskannya dalam waktu 2 jam.","Benar","Salah",
           "Salah"]
    
          ]
    elif n=='Teka-Teki Logika' and b=='Medium':
        k=[
           ["Jika semua burung memiliki sayap, dan elang adalah burung, maka:","Elang memiliki sayap"],
           ["Seorang pria memiliki dua anak. Salah satu anaknya adalah laki-laki. Apa kemungkinan anak lainnya juga laki-laki?","50%"],
           ["Ada 3 apel di keranjang. Kamu mengambil 2. Berapa banyak apel yang kamu miliki?","2"],
           ["Apa yang selalu ada di depan mata, tetapi tidak pernah bisa dilihat?","Masa Depan"],
           ["Jika dibutuhkan waktu 10 menit untuk merebus 1 butir telur,berapa waktu yang diperlukan untuk merebus 5 butir telur? ","10 menit"]
           ]
    elif n=='Teka-Teki Logika' and b=='Hard':
        k=[
          [" Apa yang hilang begitu anda menyebutkan namanya?","Diam"],
          ["Pertama kamu memakanku,lalu kamu dimakan.Aku ini apa","Kail Ikan"],
          ["Kata mana dalam kamus yang selalu salah eja?","Salah"],
          ["Tentara apa yang ukurannya kecil kecil","Tentara Sekutu"],
          ["Jika ada 10 pahlawan ikut berperang, lalu 1 diantara mereka gugur.berapa yang kembali ke markas ","1009"]
          ]
    elif n=='Sejarah' and b=='Easy':
        k=[
          ["Proklamasi Kemerdekaan Indonesia terjadi pada tanggal 17 Agustus 1945",
          "Benar","Salah","Benar"],
          ["Candi Borobudur dibangun pada masa Kerajaan Majapahit.","Benar","Salah","Salah"],
          ["Kerajaan Sriwijaya dikenal sebagai kerajaan maritim yang kuat di Nusantara.","Benar","Salah","Benar"],
          ["Kerajaan Mataram Islam berpusat di Pulau Sumatra.","Benar","Salah","Benar"],
          ["Deklarasi Kemerdekaan Indonesia dibacakan oleh Soekarno dan Mohammad Hatta.","Benar","Salah","Benar"]
          ]
    elif n=='Sejarah' and b=='Medium':
        k=[
          ["Nippon Cahaya Asia, Nippon Pemimpin Asia, dan Nippon Pelindung Asia,adalah jargon dari organisasi propaganda yakni",
           "Gerakan Tiga A","Gerakan Tiga N","Putera","Asia Hokokai","Gerakan Tiga A"],
          ["Berikut ini, manakah organisasi militer yang dibentuk saat peperangan Jepang","Hokokai","Heiho","Kaikyo","Hizbullah",
            "Heiho"],
          ["Sekolah Rakyat dalam masa penjajahan Jepang disebut juga sebagai","Kokumin Gakko",
            "Koto Chu Gakko","Shun Gakko","Shoto Chu Gakko","Kokumin Gakko"],
          ["Tokoh tasawuf berikut yang berasal dari kalangan walisongo adalah","Sunan Muria","Sunan Kudus","Sunan Bonang","Sunan Ampel","Sunan Bonang"],
          ["Bangsa Portugis datang di Maluku pada tahun","1510","1511","1512","1602","1512"]
          ]
    elif n=='Sejarah' and b=='Hard':
        k=[
          ["Insiden Mukden yang membuat ketegangan hubungan antara China dan Jepang terjadi di",
           "Hubei","Manchuria","Tokyo","Joseon","Manchuria"],
          ["San Min Chu I merupakan gagasan Sun Yat Sen.Seperti halnya Soekarno yang menggagas","Nasakom","Swadeshi","Marxisme","Wawasan Nusantara",
            "Nasakom"],
          ["Sosialisme adalah paham kebersamaan dan kemakmuran bersama.Salah satu contoh negara pengganutnya adalah","China",
            "Taiwan","Inggris","Australia","China"],
          ["Warga pribumi yang memiliki simpati besar terhadap kedatangan awal Jepang adalah","E.F.E Douwes Dekker","M.H Thamrin","Soekarno","Mohammad Hatta","M.H Thamrin"],
          ["Anggota BPUPKI yang memperjuangkan kesetaraan gender dalam UUD 1945 adalah","Siti Sukaptinah","Maria Ulfah","Muh Yamin","Ahmad Soebardjo","Maria Ulfah"]
          ]
    else:
        print("Soal untuk kombinasi tersebut belum tersedia.")
        return 0

    clear()
    print(" "*50 + colored('SELAMAT BERJUANG !', 'magenta', 'on_light_magenta', attrs=['bold']))
    skor = 0
    kataovibenar={
                          'kata1':'🐰(Ovi):wiih bener nii',
                          'kata2':'🐰(Ovi):beuh keren bangett',
                          'kata3':'🐰(Ovi):aku sukaa jawabanmuuu',
                          'kata4':'🐰(Ovi):hihihih benerr',
                          'kata5':'🐰(Ovi):nanananananaaa~',
                          'kata6':'🐰(Ovi):Ovii senang bangeet >.<',
                          'kata7':'🐰(Ovi):Hei kamuu pinter yaa',
                          'kata8':'🐰(Ovi):kamu suka makan buku yaa?',
                          'kata9':'🐰(Ovi):niceeeee',
                          'kata10':'🐰(Ovi):WIII BETUL'
                            }
    kataovisalah={
                                'kata1':'🐰(Ovi):salah salahh',
                                'kata2':'🐰(Ovi):hampir kerenn',
                                'kata3':'🐰(Ovi):huaaaa',
                                'kata4':'🐰(Ovi):hiks,sini Ovi peluk dulu',
                                'kata5':'🐰(Ovi):sedihnyee',
                                'kata6':'🐰(Ovi):Yuk bisa, semangatt',
                                'kata7':'🐰(Ovi):ehem,masih salah nih',
                                'kata8':'🐰(Ovi):HEY FOKUS YUK',
                                'kata9':'🐰(Ovi):Hayoyo!',
                                'kata10':'🐰(Ovi):Maksud mu apa jawab itu??'
                                }
    for soal in k:
        print()
        if len(soal) == 4:  # Soal True/False
            print(soal[0])
            for opsi in soal[1:3]:
                print(">", opsi)
            start = time.time()
            jawab = input("Jawab: ")
            end = time.time()
            if end - start > 60:
                print("Waktu Habis")
            elif jawab == soal[3]:
                print("Jawaban Benar")
                print(random.choice(list(kataovibenar.values())))
                time.sleep(2)
                skor += 1
                clear()
            else:
                print("Jawaban Salah")
                print(random.choice(list(kataovisalah.values())))
                time.sleep(2)
                skor -= 1      
                clear()
        elif len(soal) == 2:  # Soal Essay
            print(soal[0])
            start=time.time()
            jawab = input("Jawab: ")
            end = time.time()
            if end - start > 60:
                print("Waktu Habis")
            elif jawab == soal[1]:
                print("Jawaban Benar")
                print(random.choice(list(kataovibenar.values())))
                time.sleep(2)
                skor += 1
                clear()
            else:
                print("Jawaban Salah")
                print(random.choice(list(kataovisalah.values())))
                time.sleep(2)
                skor -= 1      
                clear()
        else:
            print(soal[0])
            for opsi in soal[1:5]:
                print(">", opsi)
            start = time.time()
            jawab = input("Jawab: ")
            end = time.time()
            if end - start > 60:
                    print("Waktu Habis")
            elif jawab == soal[5]:
                    print("Jawaban Benar")
                    print(random.choice(list(kataovibenar.values())))
                    time.sleep(2)
                    skor += 1
                    clear()
            else:
                    print("Jawaban Salah")
                    print(random.choice(list(kataovisalah.values())))
                    time.sleep(2)
                    skor -= 1  
                    clear()


    print("Skor:", skor)
    time.sleep(1.5)
    clear()
    print(colored(f"Skor Akhir: {skor}", "magenta", attrs=["bold"]))

    # Simpan data setelah kuis selesai
    simpan_data(bio, n, b)
    tambah_skor(bio, skor)
    return skor


#Main Program
bio = input("Nama: ")
skor = 0

# Pastikan file leaderboard ada
if not os.path.exists('Si Paling Pintar.txt'):
    with open('Si Paling Pintar.txt', 'w') as f:
        pass

# Pastikan file data_kuis ada
if not os.path.exists('data_kuis.txt'):
    with open('data_kuis.txt', 'w') as f:
        pass

while True:
    print(" "*80 + colored('🐰(Ovi): Mulai? (Ya/Tidak)', 'magenta', attrs=['bold']))
    hm = input("").strip()
    if hm.lower() == 'ya':
        awal()
        skor = tanya(bio)
    else:
        print("Mau tau siapa 'Si Paling Pintar'? (Ya/Tidak)")
        op = input("").strip()
        if op.lower() == 'ya':
            print(f"Leaderboard sudah tersimpan di file 'Si Paling Pintar.txt'. Cek file tersebut ya!")
        else:
            print(" "*80 + colored('🐰(Ovi): Balik lagi nanti ya, Si Paling Pintar ~', 'magenta', attrs=['bold']))
            break
