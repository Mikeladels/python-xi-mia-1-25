class pasien:
    #class variabel
    jumlah_pasien = 0
    #konstruktor
    def __init__(self, nama, berat, tinggi):
        self.nama = nama
        self.berat = berat
        self.tinggi = tinggi
        pasien.jumlah_pasien += 1
 
    #methode / fungsi
    def bmi(self):
        bmi = self.berat/(self.tinggi**2)
        print("BMI = ", bmi)
        if bmi < 18.5:
            print("kekurangan berat badan.")
        elif bmi > 18.5 and bmi <=24.9:
            print("berat badan ideal.")
        elif bmi > 24.9 and bmi <= 29.9:
            print("berat badan berlebih.")
        else:
            print("obesitas.")
 
    def beratIdeal(self):
        ideal = (self.tinggi*100 - 100) - (10/100 * (self.tinggi*100 - 100))
        print("BB Ideal = ", ideal)
        print("---------------------")
 
#instansiasi objek / pembuatan objek
pasien1 = pasien("Suho", 58, 1.72)
pasien2 = pasien("Chanyeol", 70, 1.85)
pasien3 = pasien("Do Kyungsoo", 60, 1.73)
pasien4 = pasien("Baekhyun", 58, 1.74)
pasien5 = pasien("Kai", 62, 1.82)
pasien6 = pasien("Sehun", 66, 1.83)
pasien7 = pasien("Jisong", 130, 1.77)
pasien8 = pasien("Jennie", 50, 1.63)
pasien9 = pasien("Lisa", 40, 1.67)
pasien10 = pasien("Rose", 46, 1.68)
#pemanggilan pasien 1
pasien1.bmi()
pasien1.beratIdeal()
#pemanggilan pasien 2
pasien2.bmi()
pasien2.beratIdeal()
 #pemanggilan pasien 3
pasien3.bmi()
pasien3.beratIdeal()
#pemanggilan pasien 4
pasien4.bmi()
pasien4.beratIdeal()
#pemanggilan pasien 5
pasien5.bmi()
pasien5.beratIdeal()
#pemanggilan pasien 6
pasien6.bmi()
pasien6.beratIdeal()
#pemanggilan pasien 7
pasien7.bmi()
pasien7.beratIdeal()
#pemanggilan pasien 8
pasien8.bmi()
pasien8.beratIdeal()
#pemanggilan pasien 9
pasien9.bmi()
pasien9.beratIdeal()
#pemanggilan pasien 10
pasien10.bmi()
pasien10.beratIdeal()
print("jumlah pasien : ", pasien.jumlah_pasien)