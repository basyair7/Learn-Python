# Object Oriented Programming 
# Method
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi")
        func()
        print("Setelah fungsi dieksekusi")
    return wrapper


class Mobil:
    warna = "Merah" # attribut
    def __init__(self, merek, kecepatan, warna=warna ): # constructor
        self.warna=warna
        self.merek=merek
        self.kecepatan=kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10
        
    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")
    
    @staticmethod
    def intro_mobil2():
        print("Ini adalah metode dari kelas Mobil")

def test1():
    @my_decorator
    def say_hello():
        print("Hello World")
        
    say_hello()

def test2():
    Mobil.intro_mobil()
    mobil1 = Mobil(merek="DicodingCar", kecepatan=160)
    # mobil1.intro_mobil()
    print(f"Merek: {mobil1.merek}\nWarna: {mobil1.warna}\nKecepatan: {mobil1.kecepatan}")
    print("\nTambah kecepatan!\n")
    mobil1.tambah_kecepatan()
    print(f"Merek: {mobil1.merek}\nWarna: {mobil1.warna}\nKecepatan: {mobil1.kecepatan}")

# test1()
test2()