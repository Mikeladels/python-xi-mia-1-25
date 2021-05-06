# INHERITANCE / PEWARISAN
# super class / parent class
class Manusia:
    # konstruktor
    def __init__(self, nama, jk, usia):
        self.nama = nama
        self.jk = jk
        self.usia = usia
    
    def info(self):
        print("Nama : {}\nJenis Kelamin : {}\nUsia : {}".format(self.nama, self.jk, self.usia))
        print("------------------------")
    
    def makan(self):
        print("Sedang makan pizza buatan chef toto")
        print("------------------------")
 
# sub class / child class
class Pelajar(Manusia):
    # konstruktor anak
    def __init__(self, nama, jk, usia, nis, nilai):
        Manusia.__init__(self, nama, jk, usia)
        self.nis = nis
        self.nilai = nilai
 
    def belajar(self):
        print("{} Sedang belajar di rumah".format(self.nama))
        print("------------------------")
 
    # methode overriding
    def makan(self):
        print("{} sedang breakfast dengan toast". format(self.nama))
        print("------------------------")
 
# sub class / child class
class Pekerja(Manusia):
    # konstruktor anak
    def __init__(self, nama, jk, usia, nip, gaji):
        Manusia.__init__(self, nama, jk, usia)
        self.nip = nip
        self.gaji = gaji
 
    def bekerja(self):
        print("{} sedang bekerja melawan babo".format(self.nama))
        print("------------------------")
 
# instansiasi objek
Mikel = Pelajar("Michelle Adelia", "Perempuan", 17, "16115", 99)
Vincenzo = Pekerja("Vincenzo Cassano", "Laki-laki", 35,"1166111155", 5000000000000)
 
#pemanggilan
Mikel.info()
Mikel.belajar()
Mikel.makan() #memanggil methode anak
Vincenzo.info()
Vincenzo.bekerja()
Vincenzo.makan() # memanggil methode induk