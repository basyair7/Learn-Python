# definisi subprogram
"""
Subprogram adalah bagian kode yang terpisah dalam sebuah program yang dapat dipanggil dari bagian lain dari program. 
Ini membantu dalam membagi program menjadi bagian-bagian yang lebih kecil dan mudah dikelola, meningkatkan keterbacaan, 
memfasilitasi pemeliharaan, dan mempromosikan penggunaan ulang kode. Subprogram dapat berupa fungsi (function) yang 
mengembalikan nilai atau prosedur (procedure) yang tidak mengembalikan nilai.
"""
"""Fungsi adalah blok kode yang dapat menerima input, melakukan pemrosesan, dan mengembalikan output. 
Hasil atau output tersebut dinyatakan dalam sebuah tipe data yang eksplisit. 
Artinya, fungsi yang dibuat dapat ditentukan untuk mengembalikan tipe data integer, string, atau lainnya."""
"""Prosedur adalah deretan instruksi yang jelas keadaan awal (initial state) dan keadaan akhirnya (final state). 
Prosedur mirip dengan program secara umum, tetapi memiliki cakupan yang kecil dan terbatas."""

def volume_persegi(panjang, lebar, tinggi):
    return panjang*lebar*tinggi

def minimal(a, b):
    if a <= b:
        return a
    else:
        return b

def greeting(name):
    print(f"Hello, my name is {name}")
    

def test1():
    p = 4; l = 4; t = 4
    v = volume_persegi(p,l,t)
    print(f"Volume persegi dengan p={p} cm, l={l} cm, dan t={t} cm adalah {v} cm^3")

def test2():
    a = 23; b = 100
    print(f"Nilai terkecil dari {a} dan {b} adalah {minimal(a, b)}")

def test3():
    greeting("basyair")

# test1()
# test2()
test3()