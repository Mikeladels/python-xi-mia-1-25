class siswa:
    #class variabel
    jumlah_siswa = 0
    #konstruktor
    def __init__(self, nama, kelas, alamat, nilai):
        self.nama = nama
        self.kelas = kelas
        self.alamat = alamat
        self.nilai = nilai
        siswa.jumlah_siswa += 1
    #methode
    def viewSiswa(self):
        print("---------------------")
        print("Data Siswa")
        print("Nama  : ", self.nama)
        print("Kelas : ", self.kelas)
        print("Alamat : ", self.alamat)
        print("---------------------")
    
    def viewNilai(self):
        print("Data Nilai")
        print("Nama : ", self.nama)
        for nilai in self.nilai:
            print("Nilai : ", nilai)
        print("---------------------")
    
    def viewKeterangan(self):
        print("Keterangan")
        print("Nama : ", self.nama)
        print("Kelas : ", self.kelas)
        rata = sum(self.nilai)/len(self.nilai)
        print("Rata-rata : ", rata)
        if rata >= 75:
            keterangan = "Lulus."
        else:
            keterangan = "Tidak lulus."
        print("Keterangan : ", keterangan)
        print("---------------------")
 
#instansiasi objek
siswa1 = siswa("Calvin Perdana Harianto", "XI MIPA 3", "Magelang", [89,67,85,47])
siswa2 = siswa("Callen Junisya Harianto", "XI MIPA 3", "Bantul", [89,97,85,87])
siswa3 = siswa("Jevon Dilivio Harianto Purba", "XI MIPA 1", "Yogyakarta", [80,77,87,97])
siswa4 = siswa("Carrin Aurensya Harianto", "XI MIPA 3", "Yogyakarta", [88,79,90,77])
siswa5 = siswa("Michelle Adelia Suwarno", "XI MIPA 5", "Yogyakarta", [98,99,100,97])
siswa6 = siswa("Michael Christianto Suwarno", "XI MIPA 5", "Yogyakarta", [95,95,97,97])
siswa7 = siswa("Evelyn Chrisanta Harianto", "XI MIPA 4", "Yogyakarta", [88,89,70,87])
siswa8 = siswa("Celine Fourticia Harainto", "XI MIPA 3", "Yogyakarta", [78,79,90,96])
siswa9 = siswa("Leon Aditya Narrayan", "XI MIPA 2", "Yogyakarta", [45,27,76,74])
siswa10 = siswa("Kenzie Vivo", "XI MIPA 2", "Yogyakarta", [66,67,58,98])
siswa11 = siswa("Evander Christian Harianto", "XI MIPA 4", "Yogyakarta", [91,96,100,90])
siswa12 = siswa("Gabriel Gracio", "XI MIPA 2", "Yogyakarta", [80,69,46,100])
#pemanggilan objek siswa 1
siswa1.viewSiswa()
siswa1.viewNilai()
siswa1.viewKeterangan()

#pemanggilan objek siswa 2
siswa2.viewSiswa()
siswa2.viewNilai()
siswa2.viewKeterangan()

#pemanggilan objek siswa 3
siswa3.viewSiswa()
siswa3.viewNilai()
siswa3.viewKeterangan()

#pemanggilan objek siswa 4
siswa4.viewSiswa()
siswa4.viewNilai()
siswa4.viewKeterangan()

#pemanggilan objek siswa 5
siswa5.viewSiswa()
siswa5.viewNilai()
siswa5.viewKeterangan()

#pemanggilan objek siswa 6
siswa6.viewSiswa()
siswa6.viewNilai()
siswa6.viewKeterangan()

#pemanggilan objek siswa 7
siswa7.viewSiswa()
siswa7.viewNilai()
siswa7.viewKeterangan()

#pemanggilan objek siswa 8
siswa8.viewSiswa()
siswa8.viewNilai()
siswa8.viewKeterangan()

#pemanggilan objek siswa 9
siswa9.viewSiswa()
siswa9.viewNilai()
siswa9.viewKeterangan()

#pemanggilan objek siswa 10
siswa10.viewSiswa()
siswa10.viewNilai()
siswa10.viewKeterangan()

#pemanggilan objek siswa 11
siswa11.viewSiswa()
siswa11.viewNilai()
siswa11.viewKeterangan()

#pemanggilan objek siswa 12
siswa12.viewSiswa()
siswa12.viewNilai()
siswa12.viewKeterangan()
print("Jumlah siswa : ", siswa.jumlah_siswa)