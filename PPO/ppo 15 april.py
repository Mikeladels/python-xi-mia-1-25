class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0
 
    def __init__(self, nama, umur, jabatan, gaji):
        self.nama = nama
        self.umur = umur
        self.jabatan = jabatan
        self.gaji = gaji
        
        Karyawan.jumlah_karyawan += 1
 
    def tampilkan_jumlah(self):
        print("Total karyawan:", Karyawan.jumlah_karyawan)
 
    def tampilkan_profil(self):
        print("Nama : ", self.nama)
        print("Umur : ", self.umur)
        print("Jabatan : ", self.jabatan)
        print("Gaji : ", self.gaji)
        
 
# Membuat objek pertama dari kelas Karyawan
karyawan1 = Karyawan("Atta Halilintar", "26 tahun",  "Captain", 1000000000)
# Membuat objek kedua dari kelas Karyawan
karyawan2 = Karyawan("Sohwa Halilintar", "24 tahun", "Designer", 250000000)
# Membuat objek ketiga dari kelas Karyawan
karyawan3 = Karyawan("Sajidah Halilintar", "23 tahun", "Chef", 200000000)
# Membuat objek keempat dari kelas Karyawan
karyawan4 = Karyawan("Thariq Halilintar", "22 tahun",  "Housekeeping", 100000000)
# Membuat objek kelima dari kelas Karyawan
karyawan5 = Karyawan("Iyyah Halilintar", "20 tahun", "Babbysitter",50000000)
# Membuat objek keenam dari kelas Karyawan
karyawan6 = Karyawan("Saaih Halilintar", "19 tahun",  "IT Maintanence",500000000)
# Membuat objek ketujuh dari kelas Karyawan
karyawan7 = Karyawan("Fatimah Halilintar", "17 tahun", "Babysitter",50000000)
# Membuat objek kedelapan dari kelas Karyawan
karyawan8 = Karyawan("Fateh Halilintar", "15 tahun", "Housekeeping",100000000)
# Membuat objek kesembilan dari kelas Karyawan
karyawan9 = Karyawan("Muntaz Halilintar", "12 tahun", "Presenter",150000000)
# Membuat objek kesepuluh dari kelas Karyawan
karyawan10 = Karyawan("Saleha Halilintar", "10 tahun", "Housekeeping",100000000)
# Membuat objek kesebelas dari kelas Karyawan
karyawan11 = Karyawan("Qahtan Halilintar", "9 tahun", "Housekeeping",100000000)
 
karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
karyawan3.tampilkan_profil()
karyawan4.tampilkan_profil()
karyawan5.tampilkan_profil()
karyawan6.tampilkan_profil()
karyawan7.tampilkan_profil()
karyawan8.tampilkan_profil()
karyawan9.tampilkan_profil()
karyawan10.tampilkan_profil()
karyawan11.tampilkan_profil()
print("Total karyawan :", Karyawan.jumlah_karyawan)
