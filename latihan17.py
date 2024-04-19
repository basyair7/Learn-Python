# Object Oriented Programming
# Pewarisan (Inheritance)

class Mobil: # Class Induk
    warna = "Merah" # attribut
    def __init__(self, merek, kecepatan, warna=warna ): # constructor
        self.warna=warna
        self.merek=merek
        self.kecepatan=kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10
        
class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
        
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("\nKecepatan anda meningkat, hati-hati!")
        
def test1():
    mobil_sport_1 = MobilSport(merek="Ferrari", warna="Kuning", kecepatan=160)
    print("kecepatan awal : ",mobil_sport_1.kecepatan)
    mobil_sport_1.tambah_kecepatan()
    print("tambah kecepatan +10 : ", mobil_sport_1.kecepatan)
    mobil_sport_1.turbo()
    print("tambah turbo +50 : ",mobil_sport_1.kecepatan)


test1()