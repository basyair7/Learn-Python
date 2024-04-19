# Object Oriented Programming 
# Class, Object, Attribut

class Mobil:
    warna = "Merah" # attribut
    def __init__(self, merek, kecepatan, warna=warna ): # constructor
        self.warna=warna
        self.merek=merek
        self.kecepatan=kecepatan
        
def test1():
    mobil1 = Mobil('DicodingCar', 160)
    print(mobil1.merek)
    print(mobil1.warna)
    print(mobil1.kecepatan)
    

test1()