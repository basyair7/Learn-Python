"""
TODO:
1. Buatlah class bernama Animal dengan ketentuan:
    - Memiliki properti:
      - name: string
      - age: int
      - species: string
    - Memiliki constructor untuk menginisialisasi properti:
      - name
      - age
      - species
2. Buatlah class bernama Cat dengan ketentuan:
    - Merupakan turunan dari class Animal
    - Memiliki method:
      - bernama "deskripsi" yang mengembalikan nilai string berikut ini.
        "{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
      - bernama "suara" yang akan mengembalikan nilai string "meow!"
 3. Buatlah instance dari kelas Cat bernama "myCat" dengan ketentuan:
    - Atribut name bernilai: "Neko"
    - Atribut age bernilai: 3
    - Atribut species bernilai: "Persian".
"""

#TODO: Silakan buat kode Anda di bawah ini.
class Animal:
  def __init__(this, name, age, species):
    this.name = name
    this.age = age
    this.species = species

class Cat(Animal):
  def deskripsi(this):
    return f"{this.name} adalah kucing berjenis {this.species} yang sudah berumur {this.age} tahun"
  
  def suara(this):
    return "meow!"
  
# Buat instance dari kelas myCat
myCat = Cat(name="Neko", age=3, species="Persian")
print(myCat.deskripsi())
print(myCat.suara())